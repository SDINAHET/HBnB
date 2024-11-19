# Initialization for v1 endpoints
from flask import Blueprint
from flask_restx import Api

from .users import api as users_ns
from .places import api as places_ns
from .reviews import api as reviews_ns
from .amenities import api as amenities_ns

# Create a blueprint for version 1 of the API
v1 = Blueprint('v1', __name__, url_prefix='/api/v1')

# Initialize the Flask-RESTx API with the blueprint
api = Api(v1, version='1.0', title='HBnB API',
          description='A simple clone of the Airbnb service with a backend API.')

# Add namespaces for each resource
api.add_namespace(users_ns)
api.add_namespace(places_ns)
api.add_namespace(reviews_ns)
api.add_namespace(amenities_ns)
