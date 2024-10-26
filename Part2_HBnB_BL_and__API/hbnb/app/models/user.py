#!/usr/bin/python3

from marshmallow import ValidationError
import re
from typing import List, Dict
from app.models.base_entity import BaseEntity


class User(BaseEntity):
    """
    Entity representing a user in the system.

    Attributes:
        users (Dict[str, User]): Class-level storage for registered users.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        email (str): The email address of the user.
        is_admin (bool): Indicates if the user has administrative privileges.
        places (List[Place]): List of places owned by the user.
        reviews (List[Review]): List of reviews written by the user.
    """

    users: Dict[str, 'User'] = {} # Class-level storage for users

    def __init__(self, first_name, last_name, email, is_admin=False):
        """
        Initializes a User object with the provided information and registers the user.

        Args:
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
            email (str): The email address of the user.
            is_admin (bool): Indicates if the user has administrative privileges.

        Raises:
            ValidationError: If a user with the same email already exists.
        """
        super().__init__() #appelle le constructeur de BaseEntity
        self.first_name = self.validate_first_name(first_name)
        self.last_name = self.validate_last_name(last_name)
        self.email = self.validate_email(email)
        self.is_admin = is_admin  # Ajoutez cet attribut si nécessaire
        self.places: List['Place'] = []  # Places owned by the user
        self.reviews: List['Review'] = []  # Reviews written by the user
        self.register_user()  # ajout

    def register_user(self):
        """ 
        Registers the user in the class-level dictionary.
        
        Raises:
            ValidationError: If an account with the same email already exists.
        """
        # Vérifie si un utilisateur avec cet email existe déjà
        if any(user.email == self.email for user in User.users.values()):
            raise ValidationError("An account with this email already exists.")
        User.users[self.id] = self

    def validate_first_name(self, first_name):
        """ 
        Validates the first name of the user.
        
        Args:
            first_name (str): The first name to validate.

        Raises:
            ValidationError: If the first name is invalid.

        Returns:
            str: The validated first name.
        """
        if not first_name or len(first_name) > 50:
            raise ValidationError("First name must be between 1 and 50 characters.")
        return first_name

    def validate_last_name(self, last_name):
        """ 
        Validates the last name of the user.
        
        Args:
            last_name (str): The last name to validate.

        Raises:
            ValidationError: If the last name is invalid.

        Returns:
            str: The validated last name.
        """
        if not last_name or len(last_name) > 50:
            raise ValidationError("Last name must be between 1 and 50 characters.")
        return last_name

    @staticmethod
    def is_valid_email(email):
        """ 
        Validates the email format using a simple regex.
        
        Args:
            email (str): The email to validate.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(regex, email) is not None

    def validate_email(self, email):
        """ 
        Validates the email of the user.
        
        Args:
            email (str): The email to validate.

        Raises:
            ValidationError: If the email format is invalid.

        Returns:
            str: The validated email.
        """
        if not self.is_valid_email(email):
            raise ValidationError("Invalid email format.")
        return email

    def add_place(self, place):
        """ 
        Adds a place to the user's list of places.

        Args:
            place (Place): The place to add.
        """
        self.places.append(place)
        self.save()  # Update timestamp when adding a place

    def add_review(self, review):
        """ 
        Adds a review to the user's list of reviews.

        Args:
            review (Review): The review to add.
        """
        self.reviews.append(review)
        self.save()  # Update timestamp when adding a place

    def get_reviews(self):
        """ 
        Retrieves the list of reviews written by the user.
        
        Returns:
            List[Review]: The user's reviews.
        """
        return self.reviews
