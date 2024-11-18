import sys
import os
import time
import unittest
import requests
from datetime import datetime
from app.models.user import User, ValidationError

BASE_URL = "http://localhost:5000/api/v1/users/"

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestUser(unittest.TestCase):
    email_counter = 1

    def get_unique_email(self):
        """Generate a unique email address for testing."""
        return f"test_user_{TestUser.email_counter}@example.com"
        TestUser.email_counter += 1

    def setUp(self):
        """Create a default user for tests."""
        self.default_email = self.get_unique_email()
        self.user = User(first_name="John", last_name="Doe", email=self.default_email)

    def tearDown(self):
        """Optional cleanup after each test, if needed."""
        pass  # Add cleanup logic here if necessary

    def test_create_user(self):
        """Test successful user creation and error handling."""
        user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com"
        }
        response = requests.post(BASE_URL, json=user_data)
        self.assertEqual(response.status_code, 201, f"Expected 201, got {response.status_code}")
        self.assertIn("id", response.json(), "User ID not found in response")

        # Duplicate email case
        response = requests.post(BASE_URL, json=user_data)
        self.assertEqual(response.status_code, 400, f"Expected 400, got {response.status_code}")
        print(f"Error message: {response.json().get('error')}")

        # Missing email case
        invalid_user_data = {
            "first_name": "Jane",
            "last_name": "Doe"
        }
        response = requests.post(BASE_URL, json=invalid_user_data)
        self.assertEqual(response.status_code, 400, f"Expected 400, got {response.status_code}")
        print(f"Error message: {response.json().get('error')}")

    def test_get_user_by_id(self):
        """Test retrieving a user by ID and handle errors."""
        user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example2.com"
        }
        create_response = requests.post(BASE_URL, json=user_data)
        user_id = create_response.json().get("id")

        response = requests.get(f"{BASE_URL}{user_id}")
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

        # Non-existent user ID case
        response = requests.get(f"{BASE_URL}nonexistent_id")
        self.assertEqual(response.status_code, 404, f"Expected 404, got {response.status_code}")
        print(f"Error message: {response.json().get('error')}")

    def test_list_users(self):
        """Test retrieving the list of users."""
        response = requests.get(BASE_URL)
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")
        users = response.json()
        self.assertIsInstance(users, list, "Expected a list of users")

    def test_update_user(self):
        """Test updating a user and handle errors."""
        user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": self.get_unique_email()
        }
        create_response = requests.post(BASE_URL, json=user_data)
        self.assertEqual(create_response.status_code, 201, "Failed to create user")
        user_id = create_response.json().get("id")

        updated_data = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        }
        response = requests.put(f"{BASE_URL}{user_id}", json=updated_data)
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")
        print(f"Update response: {response.json()}")

        # Edge case: Updating a non-existent user
        non_existent_id = "nonexistent_id"
        response = requests.put(f"{BASE_URL}{non_existent_id}", json=updated_data)
        self.assertEqual(response.status_code, 404, f"Expected 404, got {response.status_code}")
        print(f"Error message: {response.json().get('error')}")

if __name__ == "__main__":
    unittest.main()
