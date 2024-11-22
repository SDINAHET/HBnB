import requests
import unittest
import csv

BASE_URL = "http://127.0.0.1:5000/api/v1"
ADMIN_CREDENTIALS = {
    "first_name": "Admin",
    "last_name": "Test",
    "email": "admin_test@example.com",
    "password": "adminpassword",
    "is_admin": True
}
USER_CREDENTIALS = {
    "first_name": "Regular",
    "last_name": "Test",
    "email": "user_test@example.com",
    "password": "userpassword",
    "is_admin": False
}

class IntegrationTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create Admin and Regular User
        cls.admin_id, cls.admin_token = cls.create_user_and_authenticate(ADMIN_CREDENTIALS)
        cls.user_id, cls.user_token = cls.create_user_and_authenticate(USER_CREDENTIALS)

        # Create an Amenity
        cls.amenity_id = cls.create_amenity("WiFi", cls.admin_token)

        # Create a Place by Admin
        cls.place_id = cls.create_place("Test Place", cls.admin_id, [cls.amenity_id], cls.admin_token)

    @staticmethod
    def create_user_and_authenticate(credentials):
        # Create user
        url = f"{BASE_URL}/users/users/"
        response = requests.post(url, json=credentials)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        user_id = response.json().get('user_id')

        # Authenticate user
        auth_url = f"{BASE_URL}/auth/login"
        auth_response = requests.post(auth_url, json={"email": credentials['email'], "password": credentials['password']})
        assert auth_response.status_code == 200, f"Expected 200, got {auth_response.status_code}"
        token = auth_response.json().get('access_token')

        return user_id, token

    @staticmethod
    def create_amenity(name, token):
        url = f"{BASE_URL}/amenities/"
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        response = requests.post(url, json={"name": name}, headers=headers)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        return response.json().get('amenity_id')

    @staticmethod
    def create_place(title, owner_id, amenities, token):
        url = f"{BASE_URL}/places/"
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        data = {
            "title": title,
            "description": "Integrated Test Place",
            "price": 150.0,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "owner_id": owner_id,
            "amenities": amenities
        }
        response = requests.post(url, json=data, headers=headers)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        return response.json().get('id')

    def test_user_review_flow(self):
        """Regular user reviews the admin-created place."""
        # Create a review
        url = f"{BASE_URL}/reviews/review"
        headers = {"Authorization": f"Bearer {self.user_token}", "Content-Type": "application/json"}
        data = {"comment": "Great place!", "rating": 5, "place_id": self.place_id}
        response = requests.post(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 201)
        review_id = response.json().get('review_id')

        # Retrieve the review
        url = f"{BASE_URL}/reviews/{review_id}"
        response = requests.get(url, headers=headers)
        self.assertEqual(response.status_code, 200)

    @classmethod
    def tearDownClass(cls):
        # Save test data to CSV
        with open('test_data_integration.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["type", "id", "token"])
            writer.writerow(["admin", cls.admin_id, cls.admin_token])
            writer.writerow(["user", cls.user_id, cls.user_token])
            writer.writerow(["amenity", cls.amenity_id, None])
            writer.writerow(["place", cls.place_id, None])

if __name__ == "__main__":
    unittest.main()
