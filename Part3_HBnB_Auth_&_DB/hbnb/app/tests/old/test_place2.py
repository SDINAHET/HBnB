#!/usr/bin/python3

# hbnb/tests/test_user.py
import sys
import os
import unittest
import time
import random  # Importing random module
from datetime import datetime
# from marshmallow.exceptions import ValidationError
from marshmallow.exceptions import ValidationError

# Append the project's root directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from app.models.base_entity import BaseEntity
# , ValidationError
#from app.models.user import User, ValidationError
from app.models.user import User
# from app.models.place import Place, ValidationError
from app.models.place import Place  # Remove ValidationError from here if not used

class TestPlace(unittest.TestCase):
    def setUp(self):
        # Create a User instance for testing
        self.owner = User(
            first_name="Test",
            last_name="User",
            email=f"test_user_{int(time.time())}_{random.randint(1000, 9999)}@example.com"
        )
        # Additional setup code...

    # Your test methods here..
        self.place = Place(
            title="Beautiful Beach House",
            description="A lovely house by the beach.",
            price=150.0,
            latitude=34.0522,
            longitude=-118.2437,
            # owner=self.user
            owner=self.user  # Use self.owner here
        )

    # Your test methods here...
    def test_place_creation(self):
         self.assertIsInstance(self.place, Place)
         self.assertEqual(self.place.title, "Beautiful Beach House")
         self.assertEqual(self.place.description, "A lovely house by the beach.")
         self.assertEqual(self.place.price, 150.0)
         self.assertEqual(self.place.latitude, 34.0522)
         self.assertEqual(self.place.longitude, -118.2437)
         self.assertEqual(self.place.owner, self.user)


if __name__ == "__main__":
    unittest.main()
