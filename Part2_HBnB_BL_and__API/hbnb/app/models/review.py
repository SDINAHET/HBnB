#!/usr/bin/python3

from __future__ import annotations  # Doit être la première ligne
from .base_entity import BaseEntity
from app.models.user import User
from app.models.place import Place
from marshmallow import ValidationError
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User

class Review(BaseEntity):
    def __init__(self, comment, rating, user: User, place: Place):
        super().__init__()
        self.comment = comment
        self.rating = rating
        self.user_id = user.id
        self.place = place

    def get_user(self):
        from app.models.user import User
        return User.get_by_id(self.user_id)
