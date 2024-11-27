# hbnb/app/api/__init__.py
from flask import Blueprint

api_bp = Blueprint('api', __name__)

# Import all versioned APIs
from .v1 import api_v1_bp
api_bp.register_blueprint(api_v1_bp, url_prefix='/api/v1')
