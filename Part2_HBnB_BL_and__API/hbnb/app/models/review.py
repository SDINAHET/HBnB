#!/usr/bin/python3

# app/models/review.py
from .base_entity import BaseEntity
from .user import User
from .place import Place


class Review(BaseEntity):
    def __init__(self, comment, rating, user: User, place: Place):
        super().__init__()
        self.comment = comment
        self.rating = rating
        self.user = user
        self.place = place
