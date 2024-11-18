#!/usr/bin/python3

# run python test_user.py   --> python3 -m unittest app.tests.test_user
# root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/HBnB/HBnB/P
# art2_HBnB_BL_and__API/hbnb# python3 -m unittest app.tests.test_user

# hbnb/tests/test_user.py
import sys
import os
import unittest
from datetime import datetime

# Append the project's root directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from app.models.base_entity import BaseEntity
# , ValidationError
# from app.models.user import User, ValidationError
from app.models.user import User, ValidationError
# from app.models.user import User
# from marshmallow import ValidationError

class TestUser(unittest.TestCase):
#     # A class variable to create unique emails
#     email_counter = 1

#     def get_unique_email(self):
#        """Generate a unique email address for testing."""
#        email = f"test_user_{TestUser.email_counter}@example.com"
#        TestUser.email_counter += 1
#        return email

    def test_user_creation(self):
        # user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="secure123")
        user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.email, "john.doe@example.com")
        # self.assertEqual(user.email, user.email)
        # self.assertTrue(user.email.startswith("test_user_"))  # Check it starts with "test_user_"
        self.assertFalse(user.is_admin)  # Default value
        self.assertIsInstance(user.created_at, datetime)  # Check created_at is a datetime object
        self.assertIsInstance(user.updated_at, datetime)  # Check updated_at is a datetime object

    def test_user_invalid_email(self):
        with self.assertRaises(ValidationError):
            # User(first_name="Jane", last_name="Doe", email="invalidemail", password="password123")
            User(first_name="Jane", last_name="Doe", email="invalidemail")
    # def test_user_short_password(self):
        # with self.assertRaises(ValidationError):
            # User(first_name="Alice", last_name="Smith", email="alice.smith@example.com", password="123", isAdmin=True)

    def test_user_missing_first_name(self):
        """Test user creation with missing first name."""
        with self.assertRaises(ValidationError):
            # User(first_name="", last_name="Doe", email="jane.doe@example.com", password="password123")
            User(first_name="", last_name="Doe", email="jane.doe@example.com")

    def test_user_missing_last_name(self):
        """Test user creation with missing last name."""
        with self.assertRaises(ValidationError):
            # User(first_name="Jane", last_name="", email="jane.doe@example.com", password="password123")
            User(first_name="Jane", last_name="", email="jane.doe@example.com")

    def test_user_unique_email(self):
        """Test user creation ensuring email uniqueness."""
        # user1 = User(first_name="John", last_name="Doe", email="unique.email@example.com", password="password123")
        user1 = User(first_name="John", last_name="Doe", email="unique.email@example.com")
        with self.assertRaises(ValidationError):
            # User(first_name="Jane", last_name="Smith", email="unique.email@example.com", password="secure456")
            User(first_name="Jane", last_name="Smith", email="unique.email@example.com")

    def test_user_first_name_length(self):
        """Test user creation with first name exceeding maximum length."""
        with self.assertRaises(ValidationError):
            # User(first_name="A" * 51, last_name="Doe", email="john.doe@example.com", password="secure123")
            User(first_name="A" * 51, last_name="Doe", email="john.doe@example.com")

    def test_user_last_name_length(self):
        """Test user creation with last name exceeding maximum length."""
        with self.assertRaises(ValidationError):
            # User(first_name="John", last_name="D" * 51, email="john.doe@example.com", password="secure123")
            User(first_name="John", last_name="D" * 51, email="john.doe@example.com")

    def test_user_id_type(self):
        """Test that the user id is of the correct type."""
        # user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="secure123")
        user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
        self.assertIsInstance(user.id, str)  # Check that the id is a string

    def test_user_is_admin_default(self):
        """Test that the default value for is_admin is False."""
        # user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="secure123")
        user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
        self.assertFalse(user.is_admin)  # Check the default value of is_admin

if __name__ == "__main__":
    unittest.main()
