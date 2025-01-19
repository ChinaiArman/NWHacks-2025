"""
"""

# IMPORTS
from flask import Blueprint, jsonify, request, current_app, session

from services.decorators import verified_login_required, unverified_login_required


# DEFINE BLUEPRINT
lecture_bp = Blueprint('lecture_bp', __name__)


# ROUTES
@lecture_bp.route('/get-lectures', methods=['GET'])
@verified_login_required
def get_lectures() -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        user_id = session.get('user_id')
        lectures = db.get_lectures(user_id)
        return jsonify({"lectures": lectures}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@lecture_bp.route('/', methods=['POST'])
@verified_login_required
def create_lecture() -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        user_id = session.get('user_id')
        name = request.json.get('name')
        description = request.json.get('description')
        # TODO: add unsplash API to get random image for classroom.
        image_url = "https://img.freepik.com/premium-vector/default-image-icon-vector-missing-picture-page-website-design-mobile-app-no-photo-available_87543-11093.jpg"
        classroom_id = request.json.get('classroom_id')
        playbook_id = request.json.get('playbook_id')
        lecture = db.create_lecture(name, description, user_id, image_url, classroom_id, playbook_id)
        return jsonify({"lecture": lecture}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@lecture_bp.route('/<int:lecture_id>', methods=['GET'])
@verified_login_required
def get_lecture(lecture_id) -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        user_id = session.get('user_id')
        lecture = db.get_lecture(lecture_id, user_id)
        return jsonify({"lecture": lecture}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@lecture_bp.route('/set-inactive/<int:lecture_id>', methods=['PUT'])
@verified_login_required
def set_inactive(lecture_id) -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        user_id = session.get('user_id')
        db.set_inactive(lecture_id, user_id)
        return jsonify({"message": "lecture set inactive"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400