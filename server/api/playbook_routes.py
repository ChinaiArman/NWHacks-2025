"""
"""

# IMPORTS
from flask import Blueprint, jsonify, request, current_app, session

from services.decorators import verified_login_required

from exceptions import MissingFields


# DEFINE BLUEPRINT
playbook_bp = Blueprint('playbook_bp', __name__)


# ROUTES
@playbook_bp.route('/get-playbooks', methods=['GET'])
@verified_login_required
def get_playbook() -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        user_id = session.get('user_id')
        playbooks = db.get_playbooks(user_id)
        return jsonify({"playbook": playbooks}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@playbook_bp.route('/create-playbook', methods=['POST'])
@verified_login_required
def create_playbook() -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        user_id = session.get('user_id')
        name = request.json.get('name')
        description = request.json.get('description')
        # TODO: add unsplash API to get random image for classroom.
        image_url = "https://img.freepik.com/premium-vector/default-image-icon-vector-missing-picture-page-website-design-mobile-app-no-photo-available_87543-11093.jpg"
        playbook = db.create_playbook(name, description, user_id, image_url)
        return jsonify({"playbook": playbook}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@playbook_bp.route('/<int:classroom_id>', methods=['GET'])
@verified_login_required
def get_playbook_by_id(classroom_id: int) -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        user_id = session.get('user_id')
        playbook = db.get_playbook_by_id(classroom_id, user_id)
        return jsonify({"playbook": playbook}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@playbook_bp.route('/<int:classroom_id>', methods=['DELETE'])
@verified_login_required
def delete_playbook(classroom_id: int) -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        user_id = session.get('user_id')
        db.delete_playbook(classroom_id, user_id)
        return jsonify({"message": "playbook deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@playbook_bp.route('/get-plays/<int:playbook_id>', methods=['GET'])
@verified_login_required
def get_plays(playbook_id: int) -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        user_id = session.get('user_id')
        plays = db.get_plays(playbook_id, user_id)
        return jsonify({"plays": plays}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
