# hbnb/app/models/user.py

"""
Define the User model for the HBnB application.
"""

from app.models.base_entity import BaseEntity
from app.models import db
from flask_bcrypt import generate_password_hash, check_password_hash


class User(BaseEntity):
    """
    User model
    Represents a user in the HBnB application.
    """

    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    # Relationships
    places = db.relationship('Place', backref='owner', lazy=True)
    reviews = db.relationship('Review', backref='author', lazy=True)

    def set_password(self, password):
        """
        Hashes and sets the user's password.
        Args:
            password (str): The plaintext password to be hashed.
        """
        self.password = generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """
        Verifies if the provided password matches the stored hash.
        Args:
            password (str): The plaintext password to verify.
        Returns:
            bool: True if the password matches, False otherwise.
        """
        return check_password_hash(self.password, password)

    def to_dict(self):
        """
        Convert the User instance to a dictionary representation.
        Returns:
            dict: Dictionary representation of the User instance.
        """
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'is_admin': self.is_admin,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
