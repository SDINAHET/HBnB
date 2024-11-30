# hbnb/app/models/review.py

"""
Define the Review model for the HBnB application.
"""
from sqlalchemy import CheckConstraint

from app.models.base_entity import BaseEntity
from app.models import db


class Review(BaseEntity):
    """
    Review model
    Represents a review left by a user for a place in the HBnB application.
    """

    __tablename__ = 'reviews'

    text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    # Add the constraint to the model
    __table_args__ = (
    CheckConstraint('rating BETWEEN 1 AND 5', name='valid_rating'),
    )
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    place_id = db.Column(db.String(36), db.ForeignKey('places.id'), nullable=False)

    # Relationships
    user = db.relationship('User', backref='reviews', lazy=True)
    place = db.relationship('Place', backref='reviews', lazy=True)

    def to_dict(self):
        """
        Convert the Review instance to a dictionary representation.
        Returns:
            dict: Dictionary representation of the Review instance.
        """
        return {
            'id': self.id,
            'text': self.text,
            'rating': self.rating,
            'user_id': self.user_id,
            'place_id': self.place_id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
