#!/usr/bin/python3

# hbnb/tests/test_review.py
import sys
import os
import unittest
from datetime import datetime

# Append the project's root directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models.review import Review, ValidationError  # Adjust the import based on your project structure
from app.models.user import User  # Assuming the User class is in the models directory
from app.models.place import Place  # Assuming the Place class is in the models directory

class TestReview(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        # self.user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="secure123")
        self.user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
        self.place = Place(name="Sample Place")  # Ensure you have a valid constructor for Place
        # Add the required attributes to the Place if necessary

    def test_review_creation(self):
        """Test successful creation of a review."""
        review = Review(text="Great place!", rating=5, place=self.place, user=self.user)
        self.assertEqual(review.text, "Great place!")
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.place, self.place)
        self.assertEqual(review.user, self.user)
        self.assertIsInstance(review.created_at, datetime)  # Check created_at is a datetime object
        self.assertIsInstance(review.updated_at, datetime)  # Check updated_at is a datetime object

    def test_review_missing_text(self):
        """Test review creation with missing text."""
        with self.assertRaises(ValidationError):
            Review(text="", rating=5, place=self.place, user=self.user)  # Expect an error when text is empty

    def test_review_invalid_rating(self):
        """Test review creation with an invalid rating."""
        with self.assertRaises(ValidationError):
            Review(text="Good place.", rating=6, place=self.place, user=self.user)  # Rating must be between 1 and 5
        with self.assertRaises(ValidationError):
            Review(text="Bad place.", rating=0, place=self.place, user=self.user)  # Rating must be between 1 and 5

    def test_review_invalid_place(self):
        """Test review creation with a nonexistent place."""
        with self.assertRaises(ValidationError):
            Review(text="Nice place!", rating=5, place=None, user=self.user)  # Place must be a valid instance

    def test_review_invalid_user(self):
        """Test review creation with a nonexistent user."""
        with self.assertRaises(ValidationError):
            Review(text="Nice place!", rating=5, place=self.place, user=None)  # User must be a valid instance

    def test_review_id_type(self):
        """Test that the review id is of the correct type."""
        review = Review(text="Great place!", rating=5, place=self.place, user=self.user)
        self.assertIsInstance(review.id, str)  # Check that the id is a string

if __name__ == "__main__":
    unittest.main()
