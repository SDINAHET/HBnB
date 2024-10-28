#!/usr/bin/python3

from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns
from app.api.v1.reviews import api as reviews_ns
from app.api.v1.places import api as places_ns
from app.api.v1.amenities import api as amenities_ns
# from hbtn.app.api.v1.users import api as users_ns
# from hbtn.app.api.v1.reviews import api as reviews_ns
# from hbtn.app.api.v1.places import api as places_ns
# from hbtn.app.api.v1.amenities import api as amenities_ns

def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')
    # api = Api(app, version='1.0', title='HBnB API',
    #           description='HBnB Application API', doc='/api/v1')

    # Register the user namespace
    api.add_namespace(users_ns, path='/api/v1/users')

    # Register the reviews namespace
    api.add_namespace(reviews_ns, path='/api/v1/reviews')

    # Register the places namespace
    api.add_namespace(places_ns, path='/api/v1/places')

    # Register the amenities namespace
    api.add_namespace(amenities_ns, path='/api/v1/amenities')

    return app
