import requests
from bs4 import BeautifulSoup
from services.ai_assistant import generate_guide_content
import logging

logger = logging.getLogger(__name__)

def generate_pentest_guide(scope_url):
    try:
        scope_info = scrape_scope(scope_url)
        if not scope_info:
            raise ValueError("Failed to scrape scope information")

        guide_content = generate_guide_content(scope_info)
        return {
            'scope': scope_info,
            'guide': guide_content
        }
    except Exception as e:
        logger.error(f"Error generating pentest guide: {str(e)}")
        raise

def scrape_scope(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Failed to fetch URL {url}: {str(e)}")
        return None

    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        program_name = soup.find('h1', class_='program-name')
        program_name = program_name.text.strip() if program_name else 'Unknown Program'

        scope_info = soup.find('div', class_='scope-info')
        if not scope_info:
            logger.warning(f"No scope information found for {url}")
            return None

        description = scope_info.find('p', class_='description')
        description_text = description.text.strip() if description else ''

        targets = [target.text.strip() for target in scope_info.find_all('li', class_='target')]
        out_of_scope = [item.text.strip() for item in soup.find_all('li', class_='out-of-scope')]

        bounty_table = soup.find('table', class_='bounty-table')
        bounty_info = {}
        if bounty_table:
            rows = bounty_table.find_all('tr')
            for row in rows[1:]:
                cols = row.find_all('td')
                if len(cols) == 2:
                    bounty_info[cols[0].text.strip()] = cols[1].text.strip()

        return {
            'url': url,
            'program_name': program_name,
            'description': description_text,
            'targets': targets,
            'out_of_scope': out_of_scope,
            'bounty_info': bounty_info
        }
    except Exception as e:
        logger.error(f"Error parsing HTML from {url}: {str(e)}")
        return None