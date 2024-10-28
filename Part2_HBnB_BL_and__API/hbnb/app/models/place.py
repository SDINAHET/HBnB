#!/usr/bin/python3

from __future__ import annotations  # Doit être la première ligne
from .base_entity import BaseEntity
from app.models.user import User
from typing import List

class Place(BaseEntity):
    """
    Place entity representing a location available for rent or visit.

    Attributes:
        title (str): Title of the place.
        description (str): Description of the place.
        price (float): Price per unit (e.g., per night).
        latitude (float): Geographical latitude of the place.
        longitude (float): Geographical longitude of the place.
        owner (User): User instance representing the owner of the place.
        reviews (List[Review]): List of associated reviews.
        amenities (List[Amenity]): List of associated amenities.
    """

    def __init__(self, title, description, price, latitude, longitude, owner):
        """
        Initializes a Place object with provided information and validates it.

        Args:
            title (str): The title of the place.
            description (str): A description of the place.
            price (float): The price for renting or visiting.
            latitude (float): The latitude of the location.
            longitude (float): The longitude of the location.
            owner (User): The owner of the place.

        Raises:
            ValueError: If validation of any attribute fails.
        """
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = self.validate_latitude(latitude)
        self.longitude = self.validate_longitude(longitude)
        self.reviews: List['Review'] = []  # List to store related reviews
        self.amenities: List['Amenity'] = []  # List to store related amenities

    @staticmethod
    def validate_title(title):
        """ 
        Validates that the title is a non-empty string of max 100 characters.
        
        Args:
            title (str): The title to validate.
        
        Returns:
            str: Validated title.
        
        Raises:
            ValueError: If title is empty or exceeds 100 characters.
        """        
        if not isinstance(title, str) or len(title) == 0 or len(title) > 100:
            raise ValueError("Title must be a non-empty string with a maximum length of 100 characters")
        return title

    @staticmethod
    def validate_price(price):
        """ 
        Validates that the price is a positive float.
        
        Args:
            price (float): The price to validate.
        
        Returns:
            float: Validated price.
        
        Raises:
            ValueError: If price is not positive.
        """
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number")
        return float(price)

    @staticmethod
    def validate_latitude(latitude):
        """ 
        Validates that latitude is between -90.0 and 90.0.
        
        Args:
            latitude (float): Latitude to validate.
        
        Returns:
            float: Validated latitude.
        
        Raises:
            ValueError: If latitude is out of range.
        """
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("Latitude must be between -90.0 and 90.0")
        return latitude

    @staticmethod
    def validate_longitude(longitude):
        """ 
        Validates that longitude is between -180.0 and 180.0.
        
        Args:
            longitude (float): Longitude to validate.
        
        Returns:
            float: Validated longitude.
        
        Raises:
            ValueError: If longitude is out of range.
        """
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("Longitude must be between -180.0 and 180.0")
        return longitude

    @staticmethod
    def validate_owner(owner):
        """ 
        Validates that the owner is a valid User instance.
        
        Args:
            owner (User): Owner to validate.
        
        Returns:
            User: Validated owner.
        
        Raises:
            ValueError: If owner is not an instance of User.
        """
        if not isinstance(owner, User):
            raise ValueError("Owner must be a valid User instance")
        return owner

    def add_review(self, review: 'Review'):
        """ 
        Adds a review to the place and updates the timestamp.
        
        Args:
            review (Review): The review to add.
        """
        self.reviews.append(review)
        self.save()  # Update timestamp when modifying reviews

    def add_amenity(self, amenity: 'Amenity'):
        """ 
        Adds an amenity to the place and updates the timestamp.
        
        Args:
            amenity (Amenity): The amenity to add.
        """
        self.amenities.append(amenity)
        self.save()  # Update timestamp when modifying amenities

    def to_dict(self):
        """ 
        Returns a dictionary representation of the Place instance.
        
        Returns:
            dict: Dictionary with place details.
        """
        return {
            'id': self.id,  # Assuming BaseEntity provides an 'id' attribute
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            # 'owner': self.owner.to_dict() if self.owner else None,
            'reviews': [review.to_dict() for review in self.reviews],
            'amenities': [amenity.to_dict() for amenity in self.amenities]
        }

    def update(self, **kwargs):
        """ 
        Updates the Place instance with new values, validating each updated field.
        
        Args:
            kwargs: Dictionary containing attributes to update.

        Raises:
            ValueError: If any updated field fails validation.
        """
        if 'title' in kwargs:
            self.title = self.validate_title(kwargs['title'])
        if 'description' in kwargs:
            self.description = kwargs['description']
        if 'price' in kwargs:
            self.price = self.validate_price(kwargs['price'])
        if 'latitude' in kwargs:
            self.latitude = self.validate_latitude(kwargs['latitude'])
        if 'longitude' in kwargs:
            self.longitude = self.validate_longitude(kwargs['longitude'])
        self.save()  # Update the updated_at timestamp
