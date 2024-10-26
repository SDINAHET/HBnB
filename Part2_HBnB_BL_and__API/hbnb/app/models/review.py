#!/usr/bin/python3

from __future__ import annotations  # Doit être la première ligne
from .base_entity import BaseEntity
from app.models.user import User
from app.models.place import Place
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .place import Place

class Review(BaseEntity):
    """
    Entity representing a review of a place by a user.

    Attributes:
        comment (str): The comment provided by the user about the place.
        rating (int): The rating given by the user, which must be between 1 and 5.
        user_id (str): The ID of the user who wrote the review.
        place_id (str): The ID of the place being reviewed.
    """

    def __init__(self, comment: str, rating: int, user: User, place: Place):
        """
        Initializes a Review object with the provided information and validates it.

        Args:
            comment (str): The comment about the place.
            rating (int): The rating between 1 and 5.
            user (User): The user who is writing the review.
            place (Place): The place being reviewed.

        Raises:
            ValueError: If validation of any attribute fails.
        """
        super().__init__()
        self.comment = comment
        self.rating = rating
        self.user_id = user.id
        self.place_id = place.id
        self.validate()
        self.register_review(user, place)

    def validate(self):
        """ 
        Validates the attributes of the review.
        
        Raises:
            ValueError: If any validation checks fail.
        """
        if not isinstance(self.comment, str) or not self.comment:
            raise ValueError('Comment must be a non-empty string.')
        if not isinstance(self.rating, int) or self.rating < 1 or self.rating > 5:
            raise ValueError('Rating must be an integer between 1 and 5.')
        if not User.get_by_id(self.user_id):
            raise ValueError("User does not exist.")
        if not Place.get_by_id(self.place_id):
            raise ValueError("Place does not exist.")

    def register_review(self, user: User, place: Place):
        """ 
        Links the review to the user and the place.

        Args:
            user (User): The user who wrote the review.
            place (Place): The place being reviewed.
        """
        user.add_review(self)
        place.add_review(self)

    @staticmethod
    def get_by_id(review_id: str) -> 'Review':
        """ 
        Static method to retrieve a review by its ID.
        
        Args:
            review_id (str): The ID of the review to retrieve.
        
        Returns:
            Review: The review instance if found, otherwise None.
        """
        return next((review for review in Review.reviews.values() if review.id == review_id), None)

    def get_user(self):
        """ 
        Retrieves the user instance associated with this review.
        
        Returns:
            User: The user who wrote the review.
        """
        from app.models.user import User
        return User.get_by_id(self.user_id)

    def get_place(self):
        """ 
        Retrieves the place instance associated with this review.
        
        Returns:
            Place: The place that is being reviewed.
        """
        return Place.get_by_id(self.place_id)

    def to_dict(self):
        """ 
        Returns a dictionary representation of the Review instance.
        
        Returns:
            dict: Dictionary containing review details.
        """
        return {
            'id': self.id,
            'comment': self.comment,
            'rating': self.rating,
            'user': self.get_user().to_dict() if self.get_user() else None,
            'place': self.get_place().to_dict() if self.get_place() else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
