#!/usr/bin/python3

# app/models/place.py
from .base_entity import BaseEntity
from .review import Review
from .amenity import Amenity
from typing import List


class Place(BaseEntity):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews: List[Review] = []  # List to store related reviews
        self.amenities: List[Amenity] = []  # List to store related amenities

    def add_review(self, review: Review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity: Amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
