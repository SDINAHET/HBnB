# hbnb/__init__.py

"""
This is the root-level package for the HBnB project.
It allows the app package to be recognized and properly configured.
"""
from flask import Flask
from app.models import setup_db
from app.api import create_api

def create_app(config_name='default'):
    """Create and configure the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(f'config.{config_name}')

    # Initialize the database
    setup_db(app)

    # Register APIs
    create_api(app)

    return app
