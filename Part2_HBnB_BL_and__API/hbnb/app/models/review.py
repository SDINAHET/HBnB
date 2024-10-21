#!/usr/bin/python3

from __future__ import annotations  # Doit être la première ligne
from .base_entity import BaseEntity
from app.models.user import User
from app.models.place import Place
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User

class Review(BaseEntity):
    def __init__(self, comment: str, rating: int, user: User, place: Place):
        super().__init__()
        self.comment = comment
        self.rating = rating
        self.user_id = user.id
        self.place = place
        self.validate()

    def validate(self):
        if not isinstance(self.comment, str) or not self.comment:
            raise ValueError('Comment must be a non empty string.')
        if not isinstance(self.rating, int) or self.rating < 1 or self.rating > 5:
            raise ValueError('Rating must be an integer between 1 and 5.')

    def get_user(self):
        from app.models.user import User
        return User.get_by_id(self.user_id)
