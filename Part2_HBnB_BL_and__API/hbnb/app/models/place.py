#!/usr/bin/python3

from __future__ import annotations  # Doit être la première ligne
from .base_entity import BaseEntity


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

    def add_review(self, review: 'Review'):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity: 'Amenity'):
        """Add an amenity to the place."""
        #pass
        self.amenities.append(amenity)

    def to_dict(self):
        """Return a dictionary representation of the Place instance."""
        return {
            # 'id': self.id,  # Assuming BaseEntity provides an 'id' attribute
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner': self.owner.to_dict() if self.owner else None,
            'reviews': [review.to_dict() for review in self.reviews],
            'amenities': [amenity.to_dict() for amenity in self.amenities]
        }
