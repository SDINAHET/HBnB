#!/usr/bin/python3
# app/__init__.py

from flask import Flask
from app.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Import and register blueprints
    from app.api.v1.users import api as users_ns
    from app.api.v1.places import api as places_ns
    from app.api.v1.reviews import api as reviews_ns
    from app.api.v1.amenities import api as amenities_ns

    from flask_restx import Api
    blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
    api = Api(blueprint, version='1.0', title='HBnB API', description='HBnB Application API')

    api.add_namespace(users_ns, path='/users')
    api.add_namespace(places_ns, path='/places')
    api.add_namespace(reviews_ns, path='/reviews')
    api.add_namespace(amenities_ns, path='/amenities')

    app.register_blueprint(blueprint)

    return app
