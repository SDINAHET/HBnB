# hbnb/app/models/__init__.py

"""
Initialize models for the HBnB application.
"""

from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

def setup_db(app):
    """Set up the database with the given Flask app."""
    db.init_app(app)
    with app.app_context():
        db.create_all()

# Import models to ensure they are registered with SQLAlchemy
from app.models.base_entity import BaseEntity
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

__all__ = [
    "db",
    "setup_db",
    "BaseEntity",
    "User",
    "Place",
    "Review",
    "Amenity",
]
