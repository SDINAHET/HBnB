#!/usr/bin/python3

# hbnb/tests/test_amenity.py
import sys
import os
import unittest
from datetime import datetime

# Append the project's root directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models.amenity import Amenity, ValidationError  # Adjust the import based on your project structure

class TestAmenity(unittest.TestCase):

    def test_amenity_creation(self):
        """Test successful creation of an amenity."""
        amenity = Amenity(name="Wi-Fi")
        self.assertEqual(amenity.name, "Wi-Fi")
        self.assertIsInstance(amenity.created_at, datetime)  # Check created_at is a datetime object
        self.assertIsInstance(amenity.updated_at, datetime)  # Check updated_at is a datetime object

    def test_amenity_missing_name(self):
        """Test amenity creation with missing name."""
        with self.assertRaises(ValidationError):
            Amenity(name="")  # Expect an error when name is empty

    def test_amenity_name_length(self):
        """Test amenity creation with name exceeding maximum length."""
        with self.assertRaises(ValidationError):
            Amenity(name="A" * 51)  # Expect an error when name exceeds 50 characters

    def test_amenity_id_type(self):
        """Test that the amenity id is of the correct type."""
        amenity = Amenity(name="Wi-Fi")
        self.assertIsInstance(amenity.id, str)  # Check that the id is a string

if __name__ == "__main__":
    unittest.main()
