"""
"""

# IMPORTS
from flask import Blueprint, jsonify, request, current_app, session

from services.decorators import verified_login_required, unverified_login_required

from exceptions import MissingFields


# DEFINE BLUEPRINT
play_bp = Blueprint('play_bp', __name__)

@play_bp.route('/', methods=['POST'])
@verified_login_required
def create_play() -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        user_id = session.get('user_id')
        playbook_id = request.json.get('playbook_id')
        play_type = request.json.get('play_type')
        play_prompt = request.json.get('play_prompt')
        play_answer = request.json.get('play_answer')
        if not playbook_id or not play_type or not play_prompt:
            raise MissingFields()
        play = db.create_play(user_id, playbook_id, play_type, play_prompt, play_answer)
        return jsonify({"playbook": play}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@play_bp.route('/<int:play_id>', methods=['DELETE'])
@verified_login_required
def delete_play(play_id) -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        user_id = session.get('user_id')
        db.delete_play(play_id, user_id)
        return jsonify({"message": "play deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@play_bp.route('/<int:play_id>', methods=['GET'])
@verified_login_required
def get_play(play_id) -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        user_id = session.get('user_id')
        play = db.get_play(play_id, user_id)
        return jsonify({"play": play}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@play_bp.route('/<int:play_id>', methods=['PUT'])
@verified_login_required
def update_play(play_id) -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        user_id = session.get('user_id')
        play_type = request.json.get('play_type')
        play_prompt = request.json.get('play_prompt')
        play_answer = request.json.get('play_answer')
        if not play_type or not play_prompt or not play_answer:
            raise MissingFields()
        play = db.update_play(play_id, user_id, play_type, play_prompt, play_answer)
        return jsonify({"play": play}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@play_bp.route('/<int:play_id>/answer', methods=['POST'])
@verified_login_required
def create_play_answer(play_id) -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        user_id = session.get('user_id')
        lecture_id = request.json.get('lecture_id')
        play_answer = request.json.get('play_answer')
        if not play_answer:
            raise MissingFields()
        play = db.create_play_answer(play_id, user_id, lecture_id, play_answer)
        return jsonify({"play": play}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@play_bp.route('/<int:play_id>/answers', methods=['GET'])
@verified_login_required
def get_play_answers(play_id) -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        user_id = session.get('user_id')
        answers = db.get_play_answers(play_id, user_id)
        return jsonify({"answers": answers}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400