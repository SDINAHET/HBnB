#!/usr/bin/python3

from __future__ import annotations  # Doit être la première ligne
from .base_entity import BaseEntity
from app.models.user import User
# from app.models.review import Review  # not ok Ensure to import the Review model
from app.models.amenity import Amenity  # Ensure to import the Amenity model
from typing import List, Optional
# from typing import List

class Place(BaseEntity):
    def __init__(self, title, description, price, latitude, longitude, owner_id, owner, reviews=None, amenities= None):
    # def __init__(self, title, description, price, latitude, longitude, owner_id):
    # def __init__(self, title: str, description: Optional[str], price: float, latitude: float, longitude: float,
                #  owner_id: str, owner: 'User', reviews: Optional[List['Review']] = None,
                #  amenities: Optional[List['Amenity']] = None):
        super().__init__()

        # self.title = title
        self.title = self.validate_title(title)
        self.description = description
        # self.price = price
        self.price = self.validate_price(price)
        self.latitude = self.validate_latitude(latitude)
        self.longitude = self.validate_longitude(longitude)
        self.owner_id = owner_id  # Ensure this is included
        self.owner = owner
        # self.owner = self.validate_owner(owner)
        # self.reviews: List['Review'] = []  # List to store related reviews
        # self.amenities: List['Amenity'] = []  # List to store related amenities
        self.amenities = amenities if amenities else []
        # self.reviews = reviews if reviews is not None else []
        # self.amenities = amenities if amenities is not None else []
        # self.amenities = amenities

    @staticmethod
    def validate_title(title):
        """Validate that the title is a non-empty string with a maximum length of 100 characters."""
        if not isinstance(title, str) or len(title) == 0 or len(title) > 100:
            raise ValueError("Title must be a non-empty string with a maximum length of 100 characters")
        return title

    @staticmethod
    def validate_price(price):
        """Validate that the price is a positive float."""
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number")
        return float(price)

    @staticmethod
    def validate_latitude(latitude):
        """Validate that the latitude is within the range -90.0 to 90.0."""
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("Latitude must be between -90.0 and 90.0")
        return latitude

    @staticmethod
    def validate_longitude(longitude):
        """Validate that the longitude is within the range -180.0 to 180.0."""
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("Longitude must be between -180.0 and 180.0")
        return longitude

    @staticmethod
    def validate_owner(owner):
        """Validate that the owner is a valid User instance."""
        if not isinstance(owner, User):
            raise ValueError("Owner must be a valid User instance")
        return owner

    def add_review(self, review: 'Review'):
        """Add a review to the place."""
        self.reviews.append(review)
        self.save()  # Update timestamp when modifying reviews

    def add_amenity(self, amenity: 'Amenity'):
        """Add an amenity to the place."""
        #pass
        self.amenities.append(amenity)
        self.save()  # Update timestamp when modifying amenities

    def get_amenities(self, amenity_ids):
        amenities = []
        for amenity_id in amenity_ids:
            amenity = facade.get_amenity_by_id(amenity_id)
            if amenity:
                amenities.append({
                    'id': amenity.id,
                    'name': amenity.name
                })
        return amenities
    # amenities = self.get_amenities(place.amenities)

    #     # Optionally, you can implement an update method as discussed earlier.
    # def update(self, data: dict):
    #     """Update the Place instance with new data."""
    #     for key, value in data.items():
    #         if value is not None:  # Only update if the value is not None
    #             setattr(self, key, value)

    def to_dict(self):
        """Return a dictionary representation of the Place instance."""
        return {
            'id': self.id,  # Assuming BaseEntity provides an 'id' attribute
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner': self.owner.to_dict() if self.owner else None,
            # 'owner': self.owner.to_dict(),
            # 'reviews=[],
            'amenities': [amenity.to_dict() for amenity in self.amenities],
            # 'reviews': [review.to_dict() for review in self.reviews]
        }

    # def update(self, **kwargs):
        # """Update the Place instance with new values."""
        # try:
        #     if 'title' in kwargs:
        #         self.title = self.validate_title(kwargs['title'])
        #     if 'description' in kwargs:
        #         self.description = kwargs['description']
        #     if 'price' in kwargs:
        #         self.price = self.validate_price(kwargs['price'])
        #     if 'latitude' in kwargs:
        #         self.latitude = self.validate_latitude(kwargs['latitude'])
        #     if 'longitude' in kwargs:
        #         self.longitude = self.validate_longitude(kwargs['longitude'])
        #     if 'owner' in kwargs:
        #         self.owner = self.validate_owner(kwargs['owner'])
        #     self.save()  # Update the updated_at timestamp
        # except ValueError as err:
        #     raise ValueError(f"Invalid field data: {err}")
    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)