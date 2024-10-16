# app/models/__init__.py

from .user import User, UserSchema
from .review import Review, ReviewSchema
from .place import Place, PlaceSchema  # Supposons que vous avez une classe Place

__all__ = ['User', 'UserSchema', 'Review', 'ReviewSchema', 'Place', 'PlaceSchema']
