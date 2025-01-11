#!/usr/bin/python3

from flask import Flask
from flask_restx import Api
from app.extension import bcrypt, jwt, db
from app.api.v1.users import api as users_ns
from app.api.v1.auth import api as auth_ns
from app.api.v1.reviews import api as reviews_ns
from app.api.v1.places import api as places_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.protected import api as protected_ns
from config import config


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.config['JWT_SECRET_KEY'] = 'default_secret_key' #add SD

    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)
    

    api = Api(app, version='1.0',
            title='HBnB API',
            description='HBnB Application API',
            security='Bearer Auth', # Add SD
            authorizations={ # Add SD
              'Bearer Auth': {
                  'type': 'apiKey',
                  'in': 'header',
                  'name': 'Authorization',
                  'description': 'JWT Authorization header using the Bearer scheme. Example: "Authorization: Bearer {token}"'
                }
          })

    # Register the user namespace
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(auth_ns, path='/api/v1/auth')

    # Register the reviews namespace
    api.add_namespace(reviews_ns, path='/api/v1/reviews')

    # Register the places namespace
    api.add_namespace(places_ns, path='/api/v1/places')

    # Register the amenities namespace
    api.add_namespace(amenities_ns, path='/api/v1/amenities')

    # api.add_namespace(protected_ns, path='/api/v1')
    api.add_namespace(protected_ns, path='/api/v1/protected') # Add SD

    return app
