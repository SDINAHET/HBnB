# User model definition
from datetime import datetime
from app.models.base_entity import BaseEntity
from flask_bcrypt import generate_password_hash, check_password_hash

class User(BaseEntity):
    """
    User class representing the user entity.

    Attributes:
    -----------
    - id (str): Unique identifier for each user, inherited from BaseEntity.
    - first_name (str): The first name of the user.
    - last_name (str): The last name of the user.
    - email (str): Email address of the user, must be unique.
    - password_hash (str): Hashed password for the user.
    - is_admin (bool): Indicates whether the user has administrative privileges.
    - created_at (datetime): Timestamp when the user is created.
    - updated_at (datetime): Timestamp when the user is last updated.
    """

    def __init__(self, first_name, last_name, email, password, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password_hash = self.hash_password(password)
        self.is_admin = is_admin

    def hash_password(self, password):
        """
        Hashes the password before storing it.

        Parameters:
        -----------
        - password (str): Plain text password to be hashed.

        Returns:
        --------
        - str: Hashed password.
        """
        return generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """
        Verifies if the provided password matches the hashed password.

        Parameters:
        -----------
        - password (str): Plain text password to be verified.

        Returns:
        --------
        - bool: True if the password matches, False otherwise.
        """
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """
        Converts the user attributes to a dictionary representation for easy JSON serialization.

        Returns:
        --------
        dict: A dictionary containing the key-value pairs of the user's attributes.
        """
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'is_admin': self.is_admin,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
