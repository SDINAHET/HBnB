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
    def __init__(self, comment: str, rating: int, user: User, place: Place):
        super().__init__()
        self.comment = comment
        self.rating = rating
        self.user_id = user.id
        # self.place = place
        self.place_id = place.id
        # self.validate()
        self.register_review(user, place)

#    def validate(self):
#        if not isinstance(self.comment, str) or not self.comment:
#            raise ValueError('Comment must be a non empty string.')
#        if not isinstance(self.rating, int) or self.rating < 1 or self.rating > 5:
#            raise ValueError('Rating must be an integer between 1 and 5.')

    def validate(self):
        """Validate the review attributes."""
        if not isinstance(self.comment, str) or not self.comment:
            raise ValueError('Comment must be a non-empty string.')
        if not isinstance(self.rating, int) or self.rating < 1 or self.rating > 5:
            raise ValueError('Rating must be an integer between 1 and 5.')
        # Validation pour s'assurer que l'utilisateur et le lieu existent
        if not User.get_by_id(self.user_id):
            raise ValueError("User does not exist.")
        if not Place.get_by_id(self.place_id):
            raise ValueError("Place does not exist.")

    def register_review(self, user: User, place: Place):
        """Link the review to the user and place."""
        user.add_review(self)
        place.add_review(self)

    @staticmethod
    def get_by_id(review_id: str) -> 'Review':
        """Static method to retrieve a review by its ID."""
        return next((review for review in Review.reviews.values() if review.id == review_id), None)

    def get_user(self):
        from app.models.user import User
        return User.get_by_id(self.user_id)

    def get_place(self):
        """Retrieve the place instance associated with this review."""
        return Place.get_by_id(self.place_id)

    def to_dict(self):
        """Return a dictionary representation of the Review instance."""
        return {
            'id': self.id,
            'comment': self.comment,
            'rating': self.rating,
            'user': self.get_user().to_dict() if self.get_user() else None,
            'place': self.get_place().to_dict() if self.get_place() else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
