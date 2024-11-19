
# Initialize API namespaces for version 1
from flask_restx import Namespace

users = Namespace('users', description='User operations')
places = Namespace('places', description='Place operations')
reviews = Namespace('reviews', description='Review operations')
amenities = Namespace('amenities', description='Amenity operations')
    