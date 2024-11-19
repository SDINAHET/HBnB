import unittest
import requests
from datetime import datetime
import re

BASE_URL = "http://127.0.0.1:5000/api/v1"

class TestHBnBModelAttributes(unittest.TestCase):

    # Helper method to validate date format (for created_at and updated_at)
    def is_valid_datetime(self, date_text):
        try:
            datetime.strptime(date_text, '%Y-%m-%dT%H:%M:%S.%f')
            return True
        except ValueError:
            return False

    # User Tests
    def test_user_attributes(self):
        response = requests.post(f"{BASE_URL}/users/", json={
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com"
        })
        self.assertEqual(response.status_code, 201)
        user = response.json()

        # Test id is a string
        self.assertIsInstance(user["id"], str)

        # Test first_name and last_name lengths
        self.assertLessEqual(len(user["first_name"]), 50)
        self.assertLessEqual(len(user["last_name"]), 50)

        # Test email format
        email_pattern = r"[^@]+@[^@]+\.[^@]+"
        self.assertTrue(re.match(email_pattern, user["email"]))

        # Test is_admin default value is False
        self.assertIn("is_admin", user)
        self.assertFalse(user["is_admin"])

        # Test created_at and updated_at are valid datetime
        self.assertTrue(self.is_valid_datetime(user["created_at"]))
        self.assertTrue(self.is_valid_datetime(user["updated_at"]))

    def test_user_unique_email(self):
        # Create a second user with the same email, expecting 400 Bad Request
        response = requests.post(f"{BASE_URL}/users/", json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "john.doe@example.com"
        })
        self.assertEqual(response.status_code, 400)

    # Place Tests
    def test_place_attributes(self):
        # First, create a user as the owner
        user_response = requests.post(f"{BASE_URL}/users/", json={
            "first_name": "Owner",
            "last_name": "Place",
            "email": "owner.place@example.com"
        })
        owner_id = user_response.json()["id"]

        # Now, create a place
        response = requests.post(f"{BASE_URL}/places/", json={
            "title": "Cozy Apartment",
            "description": "A nice place to stay",
            "price": 150.0,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": owner_id
        })
        self.assertEqual(response.status_code, 201)
        place = response.json()

        # Test id is a string
        self.assertIsInstance(place["id"], str)

        # Test title length
        self.assertLessEqual(len(place["title"]), 100)

        # Test price is positive
        self.assertGreater(place["price"], 0)

        # Test latitude and longitude ranges
        self.assertTrue(-90.0 <= place["latitude"] <= 90.0)
        self.assertTrue(-180.0 <= place["longitude"] <= 180.0)

        # Test created_at and updated_at are valid datetime
        self.assertTrue(self.is_valid_datetime(place["created_at"]))
        self.assertTrue(self.is_valid_datetime(place["updated_at"]))

    # Review Tests
    def test_review_attributes(self):
        # Create a user and place to review
        user_response = requests.post(f"{BASE_URL}/users/", json={
            "first_name": "Reviewer",
            "last_name": "Test",
            "email": "reviewer@example.com"
        })
        user_id = user_response.json()["id"]

        place_response = requests.post(f"{BASE_URL}/places/", json={
            "title": "Test Place",
            "description": "For review testing",
            "price": 200.0,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "owner_id": user_id
        })
        place_id = place_response.json()["id"]

        # Create a review
        response = requests.post(f"{BASE_URL}/reviews/", json={
            "text": "Excellent stay!",
            "rating": 5,
            "user_id": user_id,
            "place_id": place_id
        })
        self.assertEqual(response.status_code, 201)
        review = response.json()

        # Test id is a string
        self.assertIsInstance(review["id"], str)

        # Test text is required
        self.assertIn("text", review)
        self.assertGreater(len(review["text"]), 0)

        # Test rating between 1 and 5
        self.assertIn("rating", review)
        self.assertTrue(1 <= review["rating"] <= 5)

        # Test created_at and updated_at are valid datetime
        self.assertTrue(self.is_valid_datetime(review["created_at"]))
        self.assertTrue(self.is_valid_datetime(review["updated_at"]))

    # Amenity Tests
    def test_amenity_attributes(self):
        response = requests.post(f"{BASE_URL}/amenities/", json={
            "name": "Wi-Fi"
        })
        self.assertEqual(response.status_code, 201)
        amenity = response.json()

        # Test id is a string
        self.assertIsInstance(amenity["id"], str)

        # Test name length is <= 50
        self.assertIn("name", amenity)
        self.assertLessEqual(len(amenity["name"]), 50)

        # Test created_at and updated_at are valid datetime
        self.assertTrue(self.is_valid_datetime(amenity["created_at"]))
        self.assertTrue(self.is_valid_datetime(amenity["updated_at"]))


if __name__ == "__main__":
    unittest.main()
