# hbnb/app/models/place.py

"""
Define the Place model for the HBnB application.
"""

from app.models.base_entity import BaseEntity
from app.models import db

class Place(BaseEntity):
    """
    Place model
    Represents a rental property in the HBnB application.
    """

    __tablename__ = 'places'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)

    # Relationships
    reviews = db.relationship('Review', backref='place', lazy=True, cascade="all, delete-orphan")
    amenities = db.relationship('Amenity', secondary='place_amenity', lazy='subquery',
                                 backref=db.backref('places', lazy=True))

    def to_dict(self):
        """
        Convert the Place instance to a dictionary representation.
        Returns:
            dict: Dictionary representation of the Place instance.
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner_id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
