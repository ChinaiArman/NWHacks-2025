"""
"""

# IMPORTS
from flask import Blueprint, jsonify, request, current_app, session

from services.decorators import unverified_login_required

from exceptions import MissingFields


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
        session.permanent = True
        return jsonify({"message": "registration successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401
    
@auth_bp.route('/check-auth-level', methods=['GET'])
def check_auth() -> tuple:
    """
    """
    try:
        if "user_id" in session:
            db = current_app.config['database']
            user = db.get_user_by_id(session.get('user_id'))
            if not user.is_verified:
                return jsonify({"auth_level": "unverified"}), 200
            else:
                return jsonify({"auth_level": "verified"}), 200
        else:
            return jsonify({"auth_level": "unauthenticated"}), 200
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 401