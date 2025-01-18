"""
"""

# IMPORTS
from flask import Blueprint, jsonify, request, current_app, session

from services.decorators import verified_login_required, unverified_login_required


# DEFINE BLUEPRINT
classroom_bp = Blueprint('classroom_bp', __name__)


# ROUTES
@classroom_bp.route('/get-student-classrooms', methods=['GET'])
@verified_login_required
def get_student_classrooms() -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        user_id = session.get('user_id')
        classrooms = db.get_student_classrooms(user_id)
        return jsonify({"classrooms": classrooms}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@classroom_bp.route('/get-teacher-classrooms', methods=['GET'])
@verified_login_required
def get_teacher_classrooms() -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        user_id = session.get('user_id')
        classrooms = db.get_teacher_classrooms(user_id)
        return jsonify({"classrooms": classrooms}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@classroom_bp.route('/', methods=['POST'])
@verified_login_required
def create_classroom() -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        authenticator = current_app.config['authenticator']
        user_id = session.get('user_id')
        name = request.json.get('name')
        # TODO: add unsplash API to get random image for classroom.
        image_url = "https://img.freepik.com/premium-vector/default-image-icon-vector-missing-picture-page-website-design-mobile-app-no-photo-available_87543-11093.jpg"
        join_code = authenticator.generate_one_time_code()
        classroom = db.create_classroom(user_id, name, image_url, join_code)
        return jsonify({"classroom": classroom}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@classroom_bp.route('/join-classroom', methods=['POST'])
@verified_login_required
def join_classroom() -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        join_code = request.json.get('join_code')
        classroom = db.get_classroom_by_join_code(join_code)
        db.add_student_to_classroom(session.get('user_id'), classroom.id)
        return jsonify({"classroom": classroom}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@classroom_bp.route('/<int:classroom_id>', methods=['GET'])
@verified_login_required
def get_classroom(classroom_id) -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        # TODO: Add check for access to classroom object.
        classroom = db.get_classroom_by_id(classroom_id)
        return jsonify({"classroom": classroom}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@classroom_bp.route('/<int:classroom_id>', methods=['DELETE'])
@verified_login_required
def delete_classroom(classroom_id) -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        db.delete_classroom(classroom_id, session.get('user_id'))
        return jsonify({"message": "classroom deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@classroom_bp.route('/<int:classroom_id>/students', methods=['GET'])
@verified_login_required
def get_classroom_students(classroom_id) -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        classroom = db.get_classroom_by_id(classroom_id)
        students = classroom.students
        return jsonify({"students": students}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@classroom_bp.route('/<int:classroom_id>/leave', methods=['GET'])
@verified_login_required
def leave_classroom(classroom_id) -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        db.leave_classroom(session.get('user_id'), classroom_id)
        return jsonify({"message": "left classroom"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400