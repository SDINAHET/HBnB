from flask import Blueprint
from flask_restx import Api

api_v1 = Blueprint('api_v1', __name__)
api = Api(api_v1)

# Import and register namespaces
from hbnb.app.api.v1.auth import api as auth_ns
from hbnb.app.api.v1.users import api as users_ns
from hbnb.app.api.v1.places import api as places_ns
from hbnb.app.api.v1.reviews import api as reviews_ns
from hbnb.app.api.v1.amenities import api as amenities_ns

api.add_namespace(auth_ns)
api.add_namespace(users_ns)
api.add_namespace(places_ns)
api.add_namespace(reviews_ns)
api.add_namespace(amenities_ns)
