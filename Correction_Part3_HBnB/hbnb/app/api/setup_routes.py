# hbnb/app/api/setup_routes.py

"""
Setup routes for the HBnB API application.
This script centralizes all route registrations.
"""

from flask import Flask
from flask_restx import Api
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.auth import api as auth_ns
from app.api.v1.users import api as users_ns
from app.api.v1.places import api as places_ns
from app.api.v1.reviews import api as reviews_ns
from app.api.v1.protected import api as protected_ns


def setup_routes(app: Flask):
    """
    Registers all API namespaces to the Flask application.

    Args:
        app (Flask): The Flask application instance.
    """
    api = Api(
        app,
        version="1.0",
        title="HBnB API",
        description="API documentation for the HBnB application",
        doc="/swagger",  # Swagger documentation URL
    )

    # Add namespaces
    api.add_namespace(auth_ns, path="/api/v1/auth")
    api.add_namespace(users_ns, path="/api/v1/users")
    api.add_namespace(places_ns, path="/api/v1/places")
    api.add_namespace(reviews_ns, path="/api/v1/reviews")
    api.add_namespace(amenities_ns, path="/api/v1/amenities")
    api.add_namespace(protected_ns, path="/api/v1/protected")
