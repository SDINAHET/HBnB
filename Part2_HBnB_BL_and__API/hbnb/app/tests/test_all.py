#!/usr/bin/python3

import sys
import os
import unittest
import requests
import json
from datetime import datetime

# Append the project's root directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from app.models.base_entity import BaseEntity
# from app.models.user import User, ValidationError
# from app.models.amenity import Amenity, ValidationError  # Adjust the import based on your project structure
# from app.models.place import Place, ValidationError
# from app.models.review import Review, ValidationError
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review

class TestModels(unittest.TestCase):

    def setUp(self):
        # User.query.filter_by(email="john.doe@example.com").delete()
        # Create a valid User instance
        self.user = User(first_name="John", last_name="Doe", email="sjohn.doe@example.com")

        # Now, use this user instance as the owner of the place
        # self.place = Place("Beach House", self.user, "A lovely beach house.", 30.0, 34.0, -118.0)

        # # Create a unique email for the user in each test
        # unique_email = f"john.doe{datetime.now().timestamp()}@example.com"
        # self.user = User("John", "Doe", unique_email)

        # self.place = Place("Beach House", self.user, "A lovely beach house.", 30.0, 34.0, -118.0)
        # self.review = Review("Great place!", 5, self.place, self.user)
        # self.amenity = Amenity("Wi-Fi")
            # Crée une instance valide de Place
        self.place = Place(
            title="Beach House",
            description="A lovely beach house.",
            price=30.0,
            latitude=34.0,
            longitude=-118.0,
            owner=self.user  # Utilise l'utilisateur comme propriétaire
        )

        # Crée une instance valide de Review
        self.review = Review(
            comment="Great place!",
            rating=5,
            user=self.user,
            place=self.place
        )

        # Crée une instance valide de Amenity
        self.amenity = Amenity(name="Wi-Fi")

    def test_user_creation(self):
        self.assertIsInstance(self.user.id, str)
        self.assertLessEqual(len(self.user.first_name), 50)
        self.assertLessEqual(len(self.user.last_name), 50)
        # self.assertRegex(self.user.email, r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        self.assertRegex(self.user.email, r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')  # best regex

    def test_place_creation(self):
        self.assertIsInstance(self.place.id, str)
        self.assertLessEqual(len(self.place.title), 100)
        self.assertGreater(self.place.price, 0)
        self.assertGreaterEqual(self.place.latitude, -90.0)
        self.assertLessEqual(self.place.latitude, 90.0)
        self.assertGreaterEqual(self.place.longitude, -180.0)
        self.assertLessEqual(self.place.longitude, 180.0)

    def test_review_creation(self):
        self.assertIsInstance(self.review.id, str)
        self.assertGreaterEqual(self.review.rating, 1)
        self.assertLessEqual(self.review.rating, 5)

    def test_amenity_creation(self):
        self.assertIsInstance(self.amenity.id, str)
        self.assertLessEqual(len(self.amenity.name), 50)

    def test_user_update(self):
        self.user.update(first_name="Jane", email="sjahn.doe@example.com")
        self.assertEqual(self.user.first_name, "Jane")
        # self.assertRegex(self.user.email, r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        self.assertRegex(self.user.email, r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')  # best regex

    def test_place_update(self):
        self.place.update(title="Ocean View House", price=200.0)
        self.assertEqual(self.place.title, "Ocean View House")
        self.assertEqual(self.place.price, 200.0)

    def test_review_update(self):
        self.review.update(text="Amazing experience!", rating=4)
        self.assertEqual(self.review.text, "Amazing experience!")
        self.assertEqual(self.review.rating, 4)

    def test_amenity_update(self):
        self.amenity.update(name="Pool")
        self.assertEqual(self.amenity.name, "Pool")

if __name__ == '__main__':
    unittest.main()
