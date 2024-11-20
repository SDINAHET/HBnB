#!/usr/bin/python3

"""
Module for managing users in a rental application.

This module defines the `User` class, which represents a user in the system.
The class inherits from `BaseEntity` and includes methods to validate attributes,
register users, and manage associated reviews and places.

Classes:
    - User: Represents a user with details such as first name, last name, email,
      admin status, owned places, and written reviews.

Attributes:
    - users (Dict[str, 'User']): Class-level dictionary to store users.

Methods:
    - __init__(first_name, last_name, email, is_admin=False): Initializes a `User` instance.
    - validate_first_name(first_name): Validates that the first name is between 1 and 50 characters.
    - validate_last_name(last_name): Validates that the last name is between 1 and 50 characters.
    - validate_email(email): Validates the email format and ensures it's unique.
    - is_valid_email(email): Checks if the email has a valid format.
    - register_user(): Registers the user in the class-level dictionary.
    - get_reviews(): Returns the list of reviews written by the user.
"""

from app.extension import bcrypt, db
from marshmallow import ValidationError
import re
from app.models.base_entity import BaseEntity
from sqlalchemy import Column, String, Integer, DateTime, Boolean
from datetime import datetime
import uuid
from flask import current_app

class User(BaseEntity):

    __tablename__ = 'users'

    id = db.Column(String(36), primary_key=True, default=str(uuid.uuid4))
    first_name = db.Column(String(100), nullable=False)
    last_name = db.Column(String(100), nullable=False)
    email = db.Column(String(100), nullable=False, unique=True)
    password = db.Column(String(255), nullable=False)
    is_admin = db.Column(Boolean, default=False)
    created_at = db.Column(DateTime, default=datetime.utcnow)
    updated_at = db.Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        """
        Initializes a new user with the provided attributes.
        """
        super().__init__() #appelle le constructeur de BaseEntity
        self.first_name = self.validate_first_name(first_name)
        self.last_name = self.validate_last_name(last_name)
        self.email = self.validate_email(email)
        self.is_admin = is_admin  # Ajoutez cet attribut si nécessaire
        self.password = password
        self.places = []  # List of places owned by the user (to be related later)
        self.reviews = []  # List of reviews written by the user (to be related later)

    def hash_password(self, password):
        """
        Hashes the password using bcrypt and stores it.
        """
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Checks if the provided password matches the stored hash."""
        current_app.logger.info(f"Hashed password: {self.password}")
        current_app.logger.info(f"Plain-text password: {password}")
        return bcrypt.check_password_hash(self.password, password)

    def validate_first_name(self, first_name):
        """Validates the first name length (1-50 characters)."""
        if not first_name or len(first_name) > 50:
            raise ValidationError("First name must be between 1 and 50 characters.")
        return first_name

    def validate_last_name(self, last_name):
        """Validates the last name length (1-50 characters)."""
        if not last_name or len(last_name) > 50:
            raise ValidationError("Last name must be between 1 and 50 characters.")
        return last_name

    def register_user(self):
        """Registers the user, ensuring unique email."""
        # Vérifie si un utilisateur avec cet email existe déjà
        if any(user.email == self.email for user in User.users.values()):
            raise ValidationError("An account with this email already exists.")
        User.users[self.id] = self

    @staticmethod
    def is_valid_email(email):
        """Validates the email format using regex."""
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(regex, email) is not None

    def validate_email(self, email):
        """Validates and ensures email is unique."""
        if not self.is_valid_email(email):
            raise ValidationError("Invalid email format.")
        return email

    def get_reviews(self):
        """Returns the list of reviews written by the user."""
        return self.reviews

    @staticmethod
    def get_by_id(user_id: str) -> 'User':
        """Fetches a user by their ID."""
        return User.query.get(user_id)  # Using SQLAlchemy's query method
    