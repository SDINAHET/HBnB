#!/usr/bin/python3

from marshmallow import ValidationError
import re
from typing import List, Dict
from app.models.base_entity import BaseEntity


class User(BaseEntity):

    users: Dict[str, 'User'] = {} # Class-level storage for users

    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__() #appelle le constructeur de BaseEntity
        self.first_name = self.validate_first_name(first_name)
        self.last_name = self.validate_last_name(last_name)
        self.email = self.validate_email(email)
        self.is_admin = is_admin  # Ajoutez cet attribut si nécessaire
        self.places: List['Place'] = []  # Places owned by the user
        self.reviews: List['Review'] = []  # Reviews written by the user
        self.register_user()  # ajout

    def validate_first_name(self, first_name):
        if not first_name or len(first_name) > 50:
            raise ValidationError("First name must be between 1 and 50 characters.")
        return first_name

    def validate_last_name(self, last_name):
        if not last_name or len(last_name) > 50:
            raise ValidationError("Last name must be between 1 and 50 characters.")
        return last_name

    def register_user(self):
        """Register the user in the class-level dictionary."""
        # Vérifie si un utilisateur avec cet email existe déjà
        if any(user.email == self.email for user in User.users.values()):
            raise ValidationError("An account with this email already exists.")
        User.users[self.id] = self

    @staticmethod
    def is_valid_email(email):
        # Simple regex for email validation
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(regex, email) is not None

    def validate_email(self, email):
        if not self.is_valid_email(email):
            raise ValidationError("Invalid email format.")
        return email

    # def add_place(self, place):
    #     """Add a place to the user's list of places."""
    #     self.places.append(place)
    #     self.save()  # Update timestamp when adding a place

    # def add_review(self, review):
    #     """Add a review to the user's list of reviews."""
    #     self.reviews.append(review)
    #     self.save()  # Update timestamp when adding a place

    def get_reviews(self):
        return self.reviews
