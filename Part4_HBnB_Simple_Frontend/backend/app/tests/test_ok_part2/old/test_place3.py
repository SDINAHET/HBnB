#!/usr/bin/python3

# hbnb/tests/test_user.py
import sys
import os
import unittest
import time
from datetime import datetime
from app.models.base_entity import ValidationError
from app.models.user import User
from app.models.place import Place

# Append the project's root directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestPlace(unittest.TestCase):

    def setUp(self):
        """Set up a User and a Place instance for testing."""
        self.user = User(
            first_name="Juhn",
            last_name="Doe",
            email=f"test_user_{int(time.time())}@example.com"  # Removed password
        )
        self.place = Place(
            title="Beautiful Beach House",
            description="A lovely house by the beach.",
            price=150.0,
            latitude=34.0522,
            longitude=-118.2437,
            owner=self.user
        )

    def test_place_creation(self):
        """Test that a Place can be created with valid attributes."""
        self.assertEqual(self.place.title, "Beautiful Beach House")
        self.assertEqual(self.place.description, "A lovely house by the beach.")
        self.assertEqual(self.place.price, 150.0)
        self.assertEqual(self.place.latitude, 34.0522)
        self.assertEqual(self.place.longitude, -118.2437)
        self.assertEqual(self.place.owner, self.user)
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_title_too_long(self):
        """Test that a title exceeding 100 characters raises ValidationError."""
        long_title = "x" * 101  # Create a title with 101 characters
        with self.assertRaises(ValidationError):
            Place(
                title=long_title,
                description="A description.",
                price=100.0,
                latitude=34.0522,
                longitude=-118.2437,
                owner=self.user
            )

    def test_title_valid_length(self):
        """Test that a title with valid length (<= 100 characters) can be created."""
        valid_title = "x" * 99  # Create a title with 99 characters
        place = Place(
            title=valid_title,
            description="A description.",
            price=100.0,
            latitude=34.0522,
            longitude=-118.2437,
            owner=self.user
        )
        self.assertEqual(place.title, valid_title)

    def test_price_negative(self):
        """Test that a negative price raises ValidationError."""
        with self.assertRaises(ValidationError):
            Place(
                title="Title",
                description="A description.",
                price=-50.0,
                latitude=34.0522,
                longitude=-118.2437,
                owner=self.user
            )

    def test_latitude_out_of_range(self):
        """Test that latitude outside the range -90.0 to 90.0 raises ValidationError."""
        with self.assertRaises(ValidationError):
            Place(
                title="Title",
                description="A description.",
                price=100.0,
                latitude=95.0,
                longitude=-118.2437,
                owner=self.user
            )

    def test_longitude_out_of_range(self):
        """Test that longitude outside the range -180.0 to 180.0 raises ValidationError."""
        with self.assertRaises(ValidationError):
            Place(
                title="Title",
                description="A description.",
                price=100.0,
                latitude=34.0522,
                longitude=200.0,
                owner=self.user
            )

    def test_owner_validation(self):
        """Test that Place raises ValidationError if owner is not a User instance."""
        with self.assertRaises(ValidationError):
            Place(
                title="Title",
                description="A description.",
                price=100.0,
                latitude=34.0522,
                longitude=-118.2437,
                owner="NotAUser"
            )

    def tearDown(self):
        """Clean up any created objects after each test if necessary."""
        pass


if __name__ == "__main__":
    unittest.main()
