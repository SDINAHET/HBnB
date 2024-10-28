#!/usr/bin/python3

import sys
import os
import unittest
import requests  # Ajout de l'import manquant
from datetime import datetime
from app.models.user import User, ValidationError

BASE_URL = "http://localhost:5000/api/v1/users/"  # Remplacez par l'URL de votre API

# Append the project's root directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestUser(unittest.TestCase):
    email_counter = 1

    def get_unique_email(self):
        """Generate a unique email address for testing."""
        email = f"test_user_{TestUser.email_counter}@example.com"
        TestUser.email_counter += 1
        return email

    def setUp(self):
        """Create a default user for tests."""
        self.default_email = self.get_unique_email()
        self.user = User(first_name="John", last_name="Doe", email=self.default_email)

    def test_user_creation(self):
        """Test successful user creation."""
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.email, self.default_email)
        self.assertFalse(self.user.is_admin)  # Default value
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_user_invalid_email(self):
        """Test user creation with an invalid email."""
        with self.assertRaises(ValidationError):
            User(first_name="Jane", last_name="Doe", email="invalidemail")

    def test_user_missing_first_name(self):
        """Test user creation with a missing first name."""
        with self.assertRaises(ValidationError):
            User(first_name="", last_name="Doe", email=self.get_unique_email())

    def test_user_missing_last_name(self):
        """Test user creation with a missing last name."""
        with self.assertRaises(ValidationError):
            User(first_name="Jane", last_name="", email=self.get_unique_email())

    def test_user_unique_email(self):
        """Test that email must be unique."""
        User(first_name="John", last_name="Doe", email=self.get_unique_email())
        with self.assertRaises(ValidationError):
            User(first_name="Jane", last_name="Smith", email=self.user.email)

    def test_user_first_name_length(self):
        """Test user creation with a first name exceeding maximum length."""
        with self.assertRaises(ValidationError):
            User(first_name="A" * 51, last_name="Doe", email=self.get_unique_email())

    def test_user_last_name_length(self):
        """Test user creation with a last name exceeding maximum length."""
        with self.assertRaises(ValidationError):
            User(first_name="John", last_name="D" * 51, email=self.get_unique_email())

    def test_user_id_type(self):
        """Test that the user id is of the correct type."""
        self.assertIsInstance(self.user.id, str)

    def test_user_is_admin_default(self):
        """Test that the default value for is_admin is False."""
        self.assertFalse(self.user.is_admin)

    def test_user_update(self):
        """Test updating user information and ensuring updated_at changes."""
        old_updated_at = self.user.updated_at
        # Pause to ensure timestamp difference
        self.user.first_name = "Jane"
        self.user.last_name = "Smith"
        self.user.email = self.get_unique_email()

        # Assuming your User model has a method to save the updated user
        self.user.save()

        # Check if the values have been updated
        self.assertEqual(self.user.first_name, "Jane")
        self.assertEqual(self.user.last_name, "Smith")
        self.assertNotEqual(self.user.email, self.default_email)

        # Check if updated_at has changed
        self.assertGreater(self.user.updated_at, old_updated_at)

if __name__ == "__main__":
    unittest.main()
