"""
"""

# IMPORTS
from functools import wraps
from flask import session, jsonify, current_app


# DECORATORS
def verified_login_required(func: callable) -> callable:
    """
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> callable:
        """
        """
        if "user_id" in session:
            db = current_app.config['database']
            user = db.get_user_by_id(session.get('user_id'))
            if user.is_verified:
                return func(*args, **kwargs)
            else:
                return jsonify({"error": "user not verified"}), 401
        else:
            return jsonify({"error": "login required"}), 401
    return wrapper

def unverified_login_required(func: callable) -> callable:
    """
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> callable:
        """
        """
        if "user_id" in session:
            return func(*args, **kwargs)
        else:
            return jsonify({"error": "login required"}), 401
    return wrapper
