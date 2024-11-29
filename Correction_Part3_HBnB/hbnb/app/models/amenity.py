# hbnb/app/models/amenity.py

"""
Define the Amenity model for the HBnB application.
"""

from app.models.base_entity import BaseEntity
from app.models import db

class Amenity(BaseEntity):
    """
    Amenity Model
    Represents an amenity that can be associated with places in the HBnB application.
    """

    __tablename__ = 'amenities'

    name = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, name: str):
        """
        Initialize an Amenity instance.
        Args:
            name (str): Name of the amenity.
        """
        self.name = name

    def to_dict(self):
        """
        Convert the Amenity object into a dictionary for API responses.
        Returns:
            dict: Dictionary representation of the Amenity.
        """
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
