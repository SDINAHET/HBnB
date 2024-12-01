#!/usr/bin/python3
"""
Module pour la gestion des entités de type 'Place' dans une application de location.

Ce module définit la classe `Place`, qui représente un lieu disponible à la location ou à la visite.
La classe hérite de `BaseEntity`, et inclut des méthodes pour valider les attributs, ajouter des avis,
ajouter des équipements et obtenir une représentation sous forme de dictionnaire de l'instance.

Classes:
    - Place: Représente un lieu avec des détails tels que le titre, la description, le prix, la latitude,
      la longitude, le propriétaire, les avis et les équipements.

Fonctions:
    - validate_title(title: str) -> str: Valide le titre du lieu.
    - validate_price(price: float) -> float: Valide le prix du lieu.
    - validate_latitude(latitude: float) -> float: Valide la latitude du lieu.
    - validate_longitude(longitude: float) -> float: Valide la longitude du lieu.
    - validate_owner(owner: User) -> User: Valide que le propriétaire est une instance de `User`.
"""

from __future__ import annotations  # Doit être la première ligne
from .base_entity import BaseEntity
from app.models.user import User
from app.extension import db

from datetime import datetime


class Place(BaseEntity):
    """
    SQLAlchemy model for the Place entity.
    """
    __tablename__ = 'places'

    id = db.Column(db.String(36), primary_key=True)  # Use String(36) for UUID
    title = db.Column(db.String(200), nullable=False)  # Title of the place
    description = db.Column(db.String(1000), nullable=False)  # Description of the place
    price = db.Column(db.Float, nullable=False)  # Price per night
    latitude = db.Column(db.Float, nullable=False)  # Latitude of the place
    longitude = db.Column(db.Float, nullable=False)  # Longitude of the place
    owner_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Creation timestamp
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)  # Update timestamp

    # Relationships
    owner = db.relationship('User', back_populates='places')  # Relation with User
    reviews = db.relationship('Review', back_populates='place', lazy=True)  # Relation with Review
    amenities = db.relationship('Amenity', secondary='place_amenities', back_populates='places', lazy='subquery')  # Relation with Amenity

    def __init__(self, title: str, description: str, price: float, latitude: float, longitude: float, owner_id: str):
        """
        Initializes a Place object with provided information and validates it.
        """
        
        if not owner_id:
            raise ValueError("Owner must be provided")
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id

    @staticmethod
    def validate_title(title):
        """
        Validates that the title is a non-empty string of max 100 characters.
        """
        if not isinstance(title, str) or len(title) == 0 or len(title) > 100:
            raise ValueError("Title must be a non-empty string with a maximum length of 100 characters")
        return title

    @staticmethod
    def validate_price(price):
        """
        Validates that the price is a positive float.
        """
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number")
        return float(price)

    @staticmethod
    def validate_latitude(latitude):
        """
        Validates that latitude is between -90.0 and 90.0.
        """
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("Latitude must be between -90.0 and 90.0")
        return latitude

    @staticmethod
    def validate_longitude(longitude):
        """
        Validates that longitude is between -180.0 and 180.0.
        """
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("Longitude must be between -180.0 and 180.0")
        return longitude

    @staticmethod
    def validate_owner(owner):
        """
        Validates that the owner is a valid User instance.
        """
        if not isinstance(owner, User):
            raise ValueError("Owner must be a valid User instance")
        return owner

    def add_review(self, review: 'Review'):
        """
        Adds a review to the place and updates the timestamp.
        """
        self.reviews.append(review)
        self.save()  # Update timestamp when modifying reviews

    def add_amenity(self, amenity: 'Amenity'):
        """
        Adds an amenity to the place and updates the timestamp.
        """
        self.amenities.append(amenity)
        self.save()  # Update timestamp when modifying amenities

    def to_dict(self):
        """
        Returns a dictionary representation of the Place instance.
        """
        return {
            'id': self.id,  # Assuming BaseEntity provides an 'id' attribute
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner': self.owner.to_dict() if self.owner else None,
            'reviews': [review.to_dict() for review in self.reviews],
            'amenities': [amenity.to_dict() for amenity in self.amenities]
        }
