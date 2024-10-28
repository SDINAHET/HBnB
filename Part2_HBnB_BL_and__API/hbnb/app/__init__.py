#!/usr/bin/python3
from flask_restx import Api
# from flask import Flask

# from app.api.v1.users import api as users_ns
# from app.api.v1.reviews import api as reviews_ns
# from app.api.v1.places import api as places_ns
# from app.api.v1.amenities import api as amenities_ns
# from hbtn.app.api.v1.users import api as users_ns
# from hbtn.app.api.v1.reviews import api as reviews_ns
# from hbtn.app.api.v1.places import api as places_ns
# from hbtn.app.api.v1.amenities import api as amenities_ns
from app.api.v1 import api
from app.api.v1.users import users_ns
from app.api.v1.places import places_ns
from app.api.v1.reviews import reviews_ns
from app.api.v1.amenities import amenities_ns
# from app.api.v1.users import register_users  # Import the function to register users
# from app.api.v1.places import register_places  # Import the function to register places


def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')
    # api = Api(app, version='1.0', title='HBnB API',
    #           description='HBnB Application API', doc='/api/v1')
    # api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc='/api/v1')
    # api.init_app(app)

    # Register the user namespace
    api.add_namespace(users_ns, path='/api/v1/users')

    # Register the reviews namespace
    api.add_namespace(reviews_ns, path='/api/v1/reviews')

    # Register the places namespace
    api.add_namespace(places_ns, path='/api/v1/places')

    # Register the amenities namespace
    api.add_namespace(amenities_ns, path='/api/v1/amenities')

    return app
