#!/usr/bin/python3

# app/models/user.py
# from marshmallow import ValidationError  # error ModuleNotFoundError: No module named 'marshmallow pip install marshmallow
# from marshmallow import Schema, fields, validate, ValidationError
# from marshmallow import ValidationError
from marshmallow import Schema, fields, post_load
import re
from typing import List, Dict
import logging

# Configuration du logging
logging.basicConfig(level=logging.DEBUG)

# Ajout d'un log pour tracer l'importation de Review
logging.debug("Importing Review in user.py")

# from .base_entity import BaseEntity
# from .place import Place
# from .review import Review
from app.models.base_entity import BaseEntity
# Ne pas importer Review directement
# from app.models.review import Review

# class ValidationError(Exception):
#     pass

# Importation différée pour éviter les importations circulaires
def get_review_schema():
    from app.models.review import ReviewSchema
    return ReviewSchema()

class User(BaseEntity):

    users: Dict[str, 'User'] = {} # Class-level storage for users

    def __init__(self, first_name, last_name, email, password, isAdmin):
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

# class UserSchema(Schema):
#     id = fields.Int(required=True)
#     name = fields.Str(required=True, validate=validate.Length(min=1))
#     email = fields.Email(required=True)

# Example usage
# user_data = {
#     "id": 1,
#     "name": "",  # This will fail validation
#     "email": "user@example.com"
# }

# user_schema = UserSchema()

# try:
#     validated_data = user_schema.load(user_data)
#     print("Validated Data:", validated_data)
# except ValidationError as err:
#     print("Validation Errors:", err.messages)

class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(load_only=True, required=True, validate=fields.Length(min=6))
    isAdmin = fields.Bool(required=True)
    reviews = fields.List(fields.Nested(get_review_schema), dump_only=True)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)
