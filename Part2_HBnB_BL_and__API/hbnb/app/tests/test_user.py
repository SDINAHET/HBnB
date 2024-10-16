#!/usr/bin/python3

# hbnb/tests/test_user.py
import sys
import os
import unittest

# Append the project's root directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from app.models.base_entity import BaseEntity
# , ValidationError
from ..models.user import User, ValidationError

class TestUser(unittest.TestCase):

    def test_user_creation(self):
        user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="secure123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.email, "john.doe@example.com")
        self.assertFalse(user.isAdmin)  # Default value

    def test_user_invalid_email(self):
        with self.assertRaises(ValidationError):
            User(first_name="Jane", last_name="Doe", email="invalidemail", password="password123")

    def test_user_short_password(self):
        with self.assertRaises(ValidationError):
            User(first_name="Alice", last_name="Smith", email="alice.smith@example.com", password="123", isAdmin=True)

if __name__ == "__main__":
    unittest.main()
