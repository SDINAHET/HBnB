# hbnb/app/api/v1/__init__.py
from flask import Blueprint

api_v1_bp = Blueprint('api_v1', __name__)

# Import endpoints
from .routes import auth, users, places, reviews, amenities, protected
api_v1_bp.register_blueprint(auth.auth_bp, url_prefix='/auth')
api_v1_bp.register_blueprint(users.users_bp, url_prefix='/users')
api_v1_bp.register_blueprint(places.places_bp, url_prefix='/places')
api_v1_bp.register_blueprint(reviews.reviews_bp, url_prefix='/reviews')
api_v1_bp.register_blueprint(amenities.amenities_bp, url_prefix='/amenities')
api_v1_bp.register_blueprint(protected.protected_bp, url_prefix='/protected')
