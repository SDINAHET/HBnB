#!/usr/bin/python3

# app/models/user.py
from marshmallow import ValidationError
import re
from typing import List, Dict
from .base_entity import BaseEntity
from .place import Place
from .review import Review



class User(BaseEntity):

    users: Dict[str, 'User'] = {} # Class-level storage for users

    def __init__(self, firstName, lastName, email, password, isAdmin):
        super().__init__() #appelle le constructeur de BaseEntity
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.isAdmin = isAdmin
        self.places: List['Place'] = []  # Places owned by the user
        self.reviews: List['Review'] = []  # Reviews written by the user
        self.validate()
        User.users[self.id] = self

    def validate(self):
        if not self.firstName or not self.lastName:
            raise ValidationError("First name and last name cannot be empty.")
        if not self.is_valid_email(self.email):
            raise ValidationError("Invalid email format.")
        if not self.password or len(self.password) < 6:
            raise ValidationError("Password must be at least 6 characters long.")

    @staticmethod
    def is_valid_email(email):
        # Simple regex for email validation
        regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.match(regex, email) is not None

    def add_place(self, place):
        """Add a place to the user's list of places."""
        self.places.append(place)

    def add_review(self, review):
        """Add a review to the user's list of reviews."""
        self.reviews.append(review)
