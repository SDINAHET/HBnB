
from flask import Flask
from flask_restx import Api
from .api.v1 import users, places, reviews, amenities

def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')
    api.add_namespace(users.api, path='/api/v1/users')
    api.add_namespace(places.api, path='/api/v1/places')
    api.add_namespace(reviews.api, path='/api/v1/reviews')
    api.add_namespace(amenities.api, path='/api/v1/amenities')
    return app
    