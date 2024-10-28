#!/usr/bin/python3

# app/models/__init__.py

# from .user import User
# from .review import Review
# from .place import Place  # Supposons que vous avez une classe Place
# from .amenity import Amenity

from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

__all__ = ['User', 'Review', 'Place', 'Amenity']
