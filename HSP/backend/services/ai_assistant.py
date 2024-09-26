import openai
from config import Config
import logging

logger = logging.getLogger(__name__)

openai.api_key = Config.OPENAI_API_KEY

def generate_guide_content(scope_info):
    try:
        prompt = f"""
        Generate a comprehensive penetration testing guide for the following scope:
        Program: {scope_info['program_name']}
        URL: {scope_info['url']}
        Description: {scope_info['description']}
        Targets: {', '.join(scope_info['targets'])}
        Out of Scope: {', '.join(scope_info['out_of_scope'])}
        Bounty Information: {scope_info['bounty_info']}

        Include detailed sections for:
        1. Reconnaissance
        2. Vulnerability Scanning
        3. Exploitation
        4. Post-Exploitation
        5. Reporting

        Provide specific tools, commands, and techniques for each section, considering the program's scope and out-of-scope items.
        """

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=3000,
            n=1,
            stop=None,
            temperature=0.7,
        )

        return response.choices[0].text.strip()
    except Exception as e:
        logger.error(f"Error generating guide content: {str(e)}")
        raise

def get_ai_insights(scope_url):
    try:
        prompt = f"""
        Analyze the bug bounty program at {scope_url} and provide key insights for a successful pentest, including:
        1. Potential high-value targets
        2. Common vulnerabilities specific to this program
        3. Recommended tools and techniques
        4. Potential challenges and how to overcome them
        5. Tips for maximizing bounty rewards
        """

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=2000,
            n=1,
            stop=None,
            temperature=0.7,
        )

        return response.choices[0].text.strip()
    except Exception as e:
        logger.error(f"Error getting AI insights: {str(e)}")
        raise