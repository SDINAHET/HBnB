# hbnb/app/api/v1/__init__.py

from flask import Blueprint
from flask_restx import Api

# Import all the namespaces
from .routes.auth import api as auth_namespace
from .routes.users import api as users_namespace
from .routes.places import api as places_namespace
from .routes.reviews import api as reviews_namespace
from .routes.amenities import api as amenities_namespace
from .routes.protected import api as protected_namespace

# Create a Blueprint for v1 API
v1_blueprint = Blueprint("api_v1", __name__, url_prefix="/api/v1")

# Set up Flask-RESTX API
api = Api(
    v1_blueprint,
    title="HBnB API",
    version="1.0",
    description="API documentation for the HBnB project (version 1)",
)

# Add namespaces to the API
api.add_namespace(auth_namespace, path="/auth")
api.add_namespace(users_namespace, path="/users")
api.add_namespace(places_namespace, path="/places")
api.add_namespace(reviews_namespace, path="/reviews")
api.add_namespace(amenities_namespace, path="/amenities")
api.add_namespace(protected_namespace, path="/protected")
