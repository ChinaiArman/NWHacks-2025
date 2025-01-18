"""
"""

# IMPORTS
from flask import Blueprint, jsonify, request, current_app, session

from services.decorators import verified_login_required, unverified_login_required


# DEFINE BLUEPRINT
email_bp = Blueprint('email_bp', __name__)