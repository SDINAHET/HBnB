import unittest
import requests
import json

BASE_URL = "http://127.0.0.1:5000/api/v1"

class TestHBnBAPI(unittest.TestCase):

    # Helper function to create sample user data
    def create_user(self, first_name, last_name, email):
        response = requests.post(f"{BASE_URL}/users/", json={
            "first_name": first_name,
            "last_name": last_name,
            "email": email
        })
        return response

    # User Tests
    def test_create_user(self):
        response = self.create_user("John", "Doe", "john.doe@example.com")
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertIn("id", data)

    def test_create_user_invalid_data(self):
        response = self.create_user("", "", "invalid-email")
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())

    def test_get_user_by_id(self):
        # First, create a user to retrieve
        response = self.create_user("Jane", "Smith", "jane.smith@example.com")
        user_id = response.json()["id"]
        # Now, get the user
        response = requests.get(f"{BASE_URL}/users/{user_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["first_name"], "Jane")

    def test_get_nonexistent_user(self):
        response = requests.get(f"{BASE_URL}/users/invalid_id")
        self.assertEqual(response.status_code, 404)

    def test_update_user(self):
        # First, create a user to update
        response = self.create_user("Jake", "Doe", "jake.doe@example.com")
        user_id = response.json()["id"]
        # Now, update the user
        response = requests.put(f"{BASE_URL}/users/{user_id}", json={
            "first_name": "Jackie",
            "last_name": "Doe"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["first_name"], "Jackie")

    # Amenity Tests
    def test_create_amenity(self):
        response = requests.post(f"{BASE_URL}/amenities/", json={
            "name": "Wi-Fi"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())

    def test_get_all_amenities(self):
        response = requests.get(f"{BASE_URL}/amenities/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_update_amenity(self):
        # First, create an amenity to update
        response = requests.post(f"{BASE_URL}/amenities/", json={"name": "Parking"})
        amenity_id = response.json()["id"]
        # Now, update the amenity
        response = requests.put(f"{BASE_URL}/amenities/{amenity_id}", json={
            "name": "Free Parking"
        })
        self.assertEqual(response.status_code, 200)

    # Place Tests
    def test_create_place(self):
        # First, create a user to be the owner
        user_response = self.create_user("Owner", "Place", "owner.place@example.com")
        owner_id = user_response.json()["id"]
        # Now, create a place
        response = requests.post(f"{BASE_URL}/places/", json={
            "title": "Cozy Apartment",
            "description": "A nice place to stay",
            "price": 100.0,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": owner_id
        })
        self.assertEqual(response.status_code, 201)

    def test_get_all_places(self):
        response = requests.get(f"{BASE_URL}/places/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_update_place(self):
        # Create a place to update
        user_response = self.create_user("Owner", "Place", "owner2.place@example.com")
        owner_id = user_response.json()["id"]
        response = requests.post(f"{BASE_URL}/places/", json={
            "title": "Apartment",
            "description": "Simple place",
            "price": 50.0,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "owner_id": owner_id
        })
        place_id = response.json()["id"]
        # Now, update the place
        response = requests.put(f"{BASE_URL}/places/{place_id}", json={
            "title": "Luxury Apartment",
            "price": 150.0
        })
        self.assertEqual(response.status_code, 200)

    # Review Tests
    def test_create_review(self):
        # Create a user and a place for the review
        user_response = self.create_user("Reviewer", "Test", "reviewer@example.com")
        user_id = user_response.json()["id"]
        place_response = requests.post(f"{BASE_URL}/places/", json={
            "title": "Test Place",
            "description": "Test Description",
            "price": 70.0,
            "latitude": 48.8566,
            "longitude": 2.3522,
            "owner_id": user_id
        })
        place_id = place_response.json()["id"]
        # Create review
        response = requests.post(f"{BASE_URL}/reviews/", json={
            "text": "Great place!",
            "rating": 5,
            "user_id": user_id,
            "place_id": place_id
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())

    def test_get_all_reviews(self):
        response = requests.get(f"{BASE_URL}/reviews/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_update_review(self):
        # Create a review to update
        user_response = self.create_user("Test", "Reviewer", "test.reviewer@example.com")
        user_id = user_response.json()["id"]
        place_response = requests.post(f"{BASE_URL}/places/", json={
            "title": "Another Place",
            "description": "Another Description",
            "price": 80.0,
            "latitude": 34.0522,
            "longitude": -118.2437,
            "owner_id": user_id
        })
        place_id = place_response.json()["id"]
        review_response = requests.post(f"{BASE_URL}/reviews/", json={
            "text": "Nice place",
            "rating": 4,
            "user_id": user_id,
            "place_id": place_id
        })
        review_id = review_response.json()["id"]
        # Now, update the review
        response = requests.put(f"{BASE_URL}/reviews/{review_id}", json={
            "text": "Amazing place!",
            "rating": 5
        })
        self.assertEqual(response.status_code, 200)

    def test_delete_review(self):
        # Create a review to delete
        user_response = self.create_user("Delete", "Review", "delete.review@example.com")
        user_id = user_response.json()["id"]
        place_response = requests.post(f"{BASE_URL}/places/", json={
            "title": "Place to be Deleted",
            "description": "Description for delete",
            "price": 90.0,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "owner_id": user_id
        })
        place_id = place_response.json()["id"]
        review_response = requests.post(f"{BASE_URL}/reviews/", json={
            "text": "Will delete",
            "rating": 3,
            "user_id": user_id,
            "place_id": place_id
        })
        review_id = review_response.json()["id"]
        # Delete review
        response = requests.delete(f"{BASE_URL}/reviews/{review_id}")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
