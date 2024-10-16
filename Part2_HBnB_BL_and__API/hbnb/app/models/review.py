#!/usr/bin/python3

# app/models/review.py
from __future__ import annotations  # Doit être la première ligne
from .base_entity import BaseEntity
# from .user import User
# from .place import Place
# Ne pas importer User directement
# from app.models.user import User
# Importer Place si nécessaire
from app.models.place import Place
# from marshmallow import Schema, fields, validate, ValidationError
# from marshmallow import ValidationError
from marshmallow import Schema, fields, post_load, ValidationError
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User

class Review(BaseEntity):
    def __init__(self, comment, rating, user: User, place: Place):
        # from .user import User
        # from .place import Place
        super().__init__()
        self.comment = comment
        self.rating = rating
        self.user_id = user.id
        self.place = place

    def get_user(self):
        from app.models.user import User
        return User.get_by_id(self.user_id)

# class ReviewSchema(Schema):
#     id = fields.Int(required=True)
#     conment = fields.Str(required=True, validate=validate.Length(min=1))
#     user_id = fields.Int(required=True)
#     place_id = fields.Int(required=True)

class ReviewSchema(Schema):
    id = fields.Str(dump_only=True)
    comment = fields.Str(required=True, validate=fields.Length(min=1))
    rating = fields.Int(required=True)
    user_id = fields.Str(required=True)
    place_id = fields.Str(required=True)

    @post_load
    def make_review(self, data, **kwargs):
        from app.models.user import User
        from app.models.place import Place

        user = User.get_by_id(data['user_id'])
        place = Place.get_by_id(data['place_id'])
        return Review(
            comment=data['comment'],
            rating=data['rating'],
            user=user,
            place=place
        )
