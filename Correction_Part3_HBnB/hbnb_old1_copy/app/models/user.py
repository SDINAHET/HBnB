from app import db, bcrypt
from app.models.base_entity import BaseEntity
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates


class User(BaseEntity):
    """
    User model for representing users in the application.

    Attributes:
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        email (str): The user's email address, unique and validated.
        password (str): The hashed password of the user.
        is_admin (bool): Whether the user is an administrator.
    """

    __tablename__ = 'users'

    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(120), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    is_admin = Column(Boolean, default=False)

    places = relationship("Place", back_populates="owner", cascade="all, delete-orphan")
    reviews = relationship("Review", back_populates="user", cascade="all, delete-orphan")

    @validates('email')
    def validate_email(self, key, value):
        """Validate that the email is not empty and follows a valid format."""
        if not value or not value.strip():
            raise ValueError("Email cannot be empty")
        if "@" not in value or "." not in value.split("@")[-1]:
            raise ValueError("Invalid email format")
        return value.strip()

    @validates('first_name', 'last_name')
    def validate_names(self, key, value):
        """Validate that the first and last names are not empty."""
        if not value or not value.strip():
            raise ValueError(f"{key.capitalize()} cannot be empty")
        if len(value) > 50:
            raise ValueError(f"{key.capitalize()} must be 50 characters or less")
        return value.strip()

    def hash_password(self, password):
        """Hash the password before storing it."""
        if not password or len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verify a provided password against the hashed password."""
        return bcrypt.check_password_hash(self.password, password)
