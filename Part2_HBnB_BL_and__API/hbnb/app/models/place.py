#!/usr/bin/python3

# app/models/place.py
from __future__ import annotations  # Doit être la première ligne
from .base_entity import BaseEntity
# from .review import Review
# from .amenity import Amenity
# from typing import List
from marshmallow import Schema, fields, post_load
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .review import Review

class Place(BaseEntity):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews: List['Review'] = []  # List to store related reviews
        self.amenities: List['Amenity'] = []  # List to store related amenities
#         self.reviews: List = []  # List to store related reviews
#         self.amenities: List = []  # List to store related amenities

    def add_review(self, review: 'Review'):
        """Add a review to the place."""
        # from .review import Review  # Import inside the method
        # if isinstance(review, Review):
        #     self.reviews.append(review)
        self.reviews.append(review)

    def add_amenity(self, amenity: 'Amenity'):
        """Add an amenity to the place."""
        # from .amenity import Amenity  # Import inside the method
        # if isinstance(amenity, Amenity):
        #     self.amenities.append(amenity)
        # self.amenities.append(amenity)
        pass

# By using 'Review' and 'Amenity' as string literals, you prevent the NameError because Python will resolve these names later when they are defined.
class PlaceSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    location = fields.Str(required=True)
    reviews = fields.List(fields.Nested(lambda: ReviewSchema()), dump_only=True)

    @post_load
    def make_place(self, data, **kwargs):
        return Place(**data)
