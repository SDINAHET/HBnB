#!/usr/bin/python3

from marshmallow import ValidationError
import re
from typing import List, Dict
from app.models.base_entity import BaseEntity


class User(BaseEntity):

    users: Dict[str, 'User'] = {} # Class-level storage for users

    def __init__(self, first_name, last_name, email, password, isAdmin=False):
        super().__init__() #appelle le constructeur de BaseEntity
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.isAdmin = isAdmin
        self.places: List['Place'] = []  # Places owned by the user
        self.reviews: List['Review'] = []  # Reviews written by the user
        self.validate()
        User.users[self.id] = self

    def validate(self):
        if not self.first_name or not self.last_name:
            raise ValidationError("First name and last name cannot be empty.")
        if not self.is_valid_email(self.email):
            raise ValidationError("Invalid email format.")
        if not self.password or len(self.password) < 6:
            raise ValidationError("Password must be at least 6 characters long.")

    @staticmethod
    def is_valid_email(email: str) -> bool:
        # Simple regex for email validation
        regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.match(regex, email) is not None

    def add_place(self, place):
        """Add a place to the user's list of places."""
        self.places.append(place)

    def add_review(self, review):
        """Add a review to the user's list of reviews."""
        from app.models.review import Review   # Import à l'intérieur de la méthode
        self.reviews.append(review)

    def get_reviews(self) -> List['Review']:
        from app.models.review import Review  # Importation retardée
        return self.reviews
