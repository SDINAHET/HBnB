import unittest
import requests

BASE_URL = "http://127.0.0.1:5000/api/v1"
ADMIN_CREDENTIALS = {
    "email": "admin@example.com",
    "password": "admin123",
    "first_name": "Admin",
    "last_name": "User",
    "is_admin": True
}
USER_CREDENTIALS = {
    "email": "user@example.com",
    "password": "user123",
    "first_name": "Regular",
    "last_name": "User",
    "is_admin": False
}

class HBnBTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up test data"""
        # Create Admin User
        response = requests.post(f"{BASE_URL}/users/", json=ADMIN_CREDENTIALS)
        cls.admin_id = response.json().get("user_id")
        cls.admin_token = cls.authenticate_user(ADMIN_CREDENTIALS)

        # Create Regular User
        response = requests.post(f"{BASE_URL}/users/", json=USER_CREDENTIALS)
        cls.user_id = response.json().get("user_id")
        cls.user_token = cls.authenticate_user(USER_CREDENTIALS)

    @staticmethod
    def authenticate_user(credentials):
        """Login and return the access token"""
        response = requests.post(f"{BASE_URL}/auth/login", json={"email": credentials["email"], "password": credentials["password"]})
        assert response.status_code == 200, "Login failed"
        return response.json().get("access_token")

    def test_create_place_as_user(self):
        """Test that a regular user can create a place"""
        headers = {"Authorization": f"Bearer {self.user_token}"}
        payload = {
            "title": "Test Place",
            "description": "A lovely place to stay.",
            "price": 150.0,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "owner_id": self.user_id
        }
        response = requests.post(f"{BASE_URL}/places/", json=payload, headers=headers)
        self.assertEqual(response.status_code, 201)
        self.place_id = response.json().get("id")

    def test_create_review_as_user(self):
        """Test that a regular user can create a review for a place"""
        headers = {"Authorization": f"Bearer {self.user_token}"}
        payload = {
            "place_id": self.place_id,
            "rating": 5,
            "comment": "Amazing place!"
        }
        response = requests.post(f"{BASE_URL}/reviews/", json=payload, headers=headers)
        self.assertEqual(response.status_code, 201)
        self.review_id = response.json().get("review_id")

    def test_admin_can_create_user(self):
        """Test that an admin can create a new user"""
        headers = {"Authorization": f"Bearer {self.admin_token}"}
        payload = {
            "email": "newuser@example.com",
            "password": "password123",
            "first_name": "New",
            "last_name": "User",
            "is_admin": False
        }
        response = requests.post(f"{BASE_URL}/users/", json=payload, headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_non_admin_cannot_create_user(self):
        """Test that a non-admin user cannot create a new user"""
        headers = {"Authorization": f"Bearer {self.user_token}"}
        payload = {
            "email": "anotheruser@example.com",
            "password": "password123",
            "first_name": "Another",
            "last_name": "User",
            "is_admin": False
        }
        response = requests.post(f"{BASE_URL}/users/", json=payload, headers=headers)
        self.assertEqual(response.status_code, 403)

    @classmethod
    def tearDownClass(cls):
        """Clean up test data"""
        headers = {"Authorization": f"Bearer {cls.admin_token}"}
        # Delete test users, places, reviews, etc.
        requests.delete(f"{BASE_URL}/users/{cls.user_id}", headers=headers)
        requests.delete(f"{BASE_URL}/users/{cls.admin_id}", headers=headers)

if __name__ == "__main__":
    unittest.main()
