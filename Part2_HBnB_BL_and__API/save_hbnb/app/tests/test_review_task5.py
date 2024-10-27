#!/usr/bin/python3

import unittest
import json
from app import create_app
from models import db, Review, Place, User

class TestReviewAPI(unittest.TestCase):

    def setUp(self):
        """Set up test client and test database"""
        self.app = create_app('testing')  # Assuming you have a testing configuration
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()  # Create the database tables

            # Create a test user and place
            self.test_user = User(id="user_test", email="test@example.com", password="password")
            self.test_place = Place(id="place_test", title="Test Place", price=100.0, latitude=45.0, longitude=-73.0, owner_id=self.test_user.id)
            db.session.add(self.test_user)
            db.session.add(self.test_place)
            db.session.commit()

    def tearDown(self):
        """Clean up after each test"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_review(self):
        """Test creating a new review"""
        data = {
            "text": "Great place to stay!",
            "rating": 5,
            "user_id": "user_test",
            "place_id": "place_test"
        }
        response = self.client.post('/api/v1/reviews/', json=data)
        self.assertEqual(response.status_code, 201)
        review_data = json.loads(response.data)
        self.assertEqual(review_data['text'], data['text'])
        self.assertEqual(review_data['rating'], data['rating'])

    def test_get_all_reviews(self):
        """Test retrieving all reviews"""
        self.test_create_review()  # Create a review to test retrieval
        response = self.client.get('/api/v1/reviews/')
        self.assertEqual(response.status_code, 200)
        reviews = json.loads(response.data)
        self.assertGreater(len(reviews), 0)  # Check that at least one review is returned

    def test_get_review(self):
        """Test retrieving a single review"""
        # First, create a review
        self.test_create_review()
        # Get the created review's ID
        response = self.client.get('/api/v1/reviews/')
        review_id = json.loads(response.data)[0]['id']
        # Now, test retrieving the review
        response = self.client.get(f'/api/v1/reviews/{review_id}')
        self.assertEqual(response.status_code, 200)
        review_data = json.loads(response.data)
        self.assertEqual(review_data['id'], review_id)

    def test_update_review(self):
        """Test updating a review"""
        # First, create a review
        self.test_create_review()
        # Get the created review's ID
        response = self.client.get('/api/v1/reviews/')
        review_id = json.loads(response.data)[0]['id']
        # Now, update the review
        update_data = {
            "text": "Amazing stay!",
            "rating": 4
        }
        response = self.client.put(f'/api/v1/reviews/{review_id}', json=update_data)
        self.assertEqual(response.status_code, 200)
        review_data = json.loads(response.data)
        self.assertEqual(review_data['message'], "Review updated successfully")
        # Verify the update was successful
        response = self.client.get(f'/api/v1/reviews/{review_id}')
        updated_review = json.loads(response.data)
        self.assertEqual(updated_review['text'], "Amazing stay!")
        self.assertEqual(updated_review['rating'], 4)

    def test_delete_review(self):
        """Test deleting a review"""
        # First, create a review
        self.test_create_review()
        # Get the created review's ID
        response = self.client.get('/api/v1/reviews/')
        review_id = json.loads(response.data)[0]['id']
        # Now, delete the review
        response = self.client.delete(f'/api/v1/reviews/{review_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Review deleted successfully", str(response.data))
        # Verify the review was deleted
        response = self.client.get(f'/api/v1/reviews/{review_id}')
        self.assertEqual(response.status_code, 404)

    def test_get_reviews_for_place(self):
        """Test retrieving all reviews for a specific place"""
        self.test_create_review()  # Create a review associated with a place
        response = self.client.get('/api/v1/places/place_test/reviews')
        self.assertEqual(response.status_code, 200)
        reviews = json.loads(response.data)
        self.assertGreater(len(reviews), 0)
        self.assertEqual(reviews[0]['place_id'], "place_test")


if __name__ == "__main__":
    unittest.main()
