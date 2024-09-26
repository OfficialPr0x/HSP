from flask import Blueprint, request, jsonify
from services.guide_generator import generate_pentest_guide
from services.ai_assistant import get_ai_insights

bp = Blueprint('guide', __name__, url_prefix='/api/guide')

@bp.route('/generate', methods=['POST'])
def generate_guide():
    data = request.json
    scope_url = data.get('scope_url')
    if not scope_url:
        return jsonify({'error': 'Scope URL is required'}), 400

    guide = generate_pentest_guide(scope_url)
    return jsonify(guide)

@bp.route('/insights', methods=['POST'])
def get_insights():
    data = request.json
    scope_url = data.get('scope_url')
    if not scope_url:
        return jsonify({'error': 'Scope URL is required'}), 400

    insights = get_ai_insights(scope_url)
    return jsonify(insights)