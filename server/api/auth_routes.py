"""
"""

# IMPORTS
from flask import Blueprint, jsonify, request, current_app, session

from services.decorators import verified_login_required, unverified_login_required


# DEFINE BLUEPRINT
auth_bp = Blueprint('auth_bp', __name__)