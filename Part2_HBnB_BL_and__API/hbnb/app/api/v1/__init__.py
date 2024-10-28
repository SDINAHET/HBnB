# #!/usr/bin/python3
# from flask_restx import Api
# from places import api as places_api
# from app.api.v1 import api
# api = Api()
# api.add_namespace(places_api)
# def create_app():
# from app.api.v1.users import users_ns

# app/api/v1/__init__.py
# from flask_restx import Api
# from app.api.v1.users import users_ns
# from app.api.v1.places import places_ns
# from app.api.v1.reviews import reviews_ns
# from app.api.v1.amenities import amenities_ns

# api = Api(version='1.0', title='HBnB API', description='HBnB Application API')

# # Register namespaces
# api.add_namespace(users_ns, path='/api/v1/users')
# api.add_namespace(reviews_ns, path='/api/v1/reviews')
# api.add_namespace(places_ns, path='/api/v1/places')
# api.add_namespace(amenities_ns, path='/api/v1/amenities')
