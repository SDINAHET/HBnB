from app import db
from app.models.base_entity import BaseEntity
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates


class Review(BaseEntity):
    """
    Review model for representing reviews in the application.

    Attributes:
        text (str): The content of the review.
        rating (int): The rating for the place, between 1 and 5.
        place_id (str): The ID of the associated place.
        user_id (str): The ID of the user who created the review.
    """

    __tablename__ = 'reviews'

    text = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    place_id = Column(String, ForeignKey('places.id', ondelete='CASCADE'), nullable=False)
    user_id = Column(String, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    place = relationship("Place", back_populates="reviews")
    user = relationship("User", back_populates="reviews")

    @validates('rating')
    def validate_rating(self, key, value):
        """Validate that the rating is between 1 and 5."""
        if not (1 <= value <= 5):
            raise ValueError("Rating must be between 1 and 5")
        return value

    @validates('text')
    def validate_text(self, key, value):
        """Validate that the review text is not empty."""
        if not value or not value.strip():
            raise ValueError("Review text cannot be empty")
        return value
