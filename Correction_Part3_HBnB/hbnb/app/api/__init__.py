# hbnb/app/api/__init__.py

from flask import Flask
from hbnb.app.api.v1 import blueprint as api_v1_blueprint

def register_blueprints(app: Flask):
    """
    Register all API blueprints with the Flask application.
    """
    app.register_blueprint(api_v1_blueprint)
