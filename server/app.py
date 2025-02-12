"""
"""

# IMPORTS
from flask import Flask, jsonify, request
from flask_cors import CORS

from services.Authenticator import Authenticator
from services.Database import Database
from services.Emailer import Emailer

from api.auth_routes import auth_bp
from api.classroom_routes import classroom_bp
from api.email_routes import email_bp
from api.playbook_routes import playbook_bp
from api.play_routes import play_bp
from api.lecture_routes import lecture_bp

from db_config import db, configure_db
from session_config import configure_sessions
from dotenv import load_dotenv
import os


# CONSTANTS
load_dotenv()
CLIENT_URL = os.getenv('CLIENT_URL')


# FLASK CONFIGURATION
def create_app():
    """
    """
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "http://" + CLIENT_URL, "allow_headers": ["Content-Type"]}}, supports_credentials=True)

    # CONFIGURE SERVICES
    app.config['database'] = Database(db)
    app.config['authenticator'] = Authenticator()
    app.config['emailer'] = Emailer()

    # DATABASE CONFIGURATION
    configure_db(app)

    # SESSION CONFIGURATION
    configure_sessions(app, db)
    
    # ROUTES
    @app.route('/', methods=['GET'])
    def root():
        return jsonify({"message": "Hello World"})
    
    @app.route('/health', methods=['GET'])
    def health():
        return jsonify({"status": "OK"}), 200
    
    # RESPONSE HEADERS
    @app.after_request
    def after_request(response):
        response.headers['Access-Control-Allow-Origin'] = CLIENT_URL
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, PATCH, DELETE, OPTIONS'
        # Handle OPTIONS request directly
        if request.method == 'OPTIONS':
            response.status_code = 200
        return response
            
    # REGISTER BLUEPRINTS
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(classroom_bp, url_prefix='/api/classroom')
    app.register_blueprint(email_bp, url_prefix='/api/email')
    app.register_blueprint(playbook_bp, url_prefix='/api/playbook')
    app.register_blueprint(play_bp, url_prefix='/api/play')
    app.register_blueprint(lecture_bp, url_prefix='/api/lecture')

    return app, db
