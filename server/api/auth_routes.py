"""
"""

# IMPORTS
from flask import Blueprint, jsonify, request, current_app, session

from services.decorators import verified_login_required, unverified_login_required

from exceptions import EmailAlreadyExists, MissingFields


# DEFINE BLUEPRINT
auth_bp = Blueprint('auth_bp', __name__)


# ROUTES
@auth_bp.route('/login', methods=['POST'])
def login() -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        authenticator = current_app.config['authenticator']
        email = request.json.get('email')
        password = request.json.get('password')
        user = db.get_user_by_email(email)
        authenticator.verify_password(password, user.password)
        session.permanent = True
        session['user_id'] = user.id
        return jsonify({"message": "login successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401
    
@auth_bp.route('/logout', methods=['POST'])
@unverified_login_required
def logout() -> tuple:
    """
    """
    try:
        session.clear()
        return jsonify({"message": "logout successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401
    
@auth_bp.route('/register', methods=['POST'])
def register() -> tuple:
    """
    """
    try:
        db = current_app.config['database']
        authenticator = current_app.config['authenticator']
        email = request.json.get('email')
        username = request.json.get('username')
        password = request.json.get('password')
        # TODO: Implement email verification with one time code + email service.
        if not username or not email or not password:
            raise MissingFields()
        user = db.create_user(username, email, authenticator.encrypt_password(password))
        session['user_id'] = user.id
        return jsonify({"message": "registration successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401
    
@auth_bp.route('/is-verified', methods=['GET'])
@verified_login_required
def is_verified() -> tuple:
    """
    """
    try:
        return jsonify({"message": "User is verified"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401
    
@auth_bp.route('/is-unverified', methods=['GET'])
@unverified_login_required
def is_unverified() -> tuple:
    """
    """
    try:
        return jsonify({"message": "User is unverified"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401