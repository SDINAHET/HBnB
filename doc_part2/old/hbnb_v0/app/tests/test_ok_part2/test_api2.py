import requests
import unittest

BASE_URL = "http://127.0.0.1:5000/api/v1"
USER_CREDENTIALS = {
    "first_name": "Test",
    "last_name": "User",
    "email": "testuser@example.com",
    "password": "password123"
}

class APITestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user_id = cls.create_user()
        cls.token = cls.authenticate_user()
        cls.amenity_id_1 = cls.create_amenity("WiFi")
        cls.amenity_id_2 = cls.create_amenity("Pool")

    @staticmethod
    def create_user():
        url = f"{BASE_URL}/users/"
        response = requests.post(url, json=USER_CREDENTIALS)
        print("Create User:", response.status_code, response.json())
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        return response.json().get('id')

    @staticmethod
    def authenticate_user():
        url = f"{BASE_URL}/auth/login"
        data = {
            "email": USER_CREDENTIALS['email'],
            "password": USER_CREDENTIALS['password']
        }
        response = requests.post(url, json=data)
        print("Authenticate User:", response.status_code, response.json())
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        return response.json().get('access_token')

    @classmethod
    def create_amenity(cls, name):
        url = f"{BASE_URL}/amenities/"
        headers = {
            "Authorization": f"Bearer {cls.token}",
            "Content-Type": "application/json"
        }
        data = {
            "name": name
        }
        response = requests.post(url, json=data, headers=headers)
        print(f"Create Amenity ({name}):", response.status_code, response.json())
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        return response.json().get('id')

    def test_place_creation(self):
        url = f"{BASE_URL}/places/"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        data = {
            "title": "New Place",
            "description": "A nice place",
            "price": 100.0,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": self.user_id,
            "amenities": [self.amenity_id_1, self.amenity_id_2]
        }
        response = requests.post(url, json=data, headers=headers)
        print("Test Place Creation:", response.status_code)
        if response.status_code == 201:
            print(response.json())
            self.place_id = response.json().get('id')
        else:
            print(response.text)
        self.assertEqual(response.status_code, 201, f"Expected 201, got {response.status_code}")

    def test_unauthorized_place_update(self):
        if not hasattr(self, 'place_id'):
            self.skipTest("Place creation failed, skipping test_unauthorized_place_update")
        url = f"{BASE_URL}/places/{self.place_id}"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        data = {
            "title": "Updated Place",
            "description": "An updated nice place",
            "price": 150.0,
            "latitude": 37.7749,
            "longitude": -122.4194
        }
        response = requests.put(url, json=data, headers=headers)
        print("Test Unauthorized Place Update:", response.status_code, response.json())
        self.assertEqual(response.status_code, 403, f"Expected 403, got {response.status_code}")

    def test_create_review(self):
        if not hasattr(self, 'place_id'):
            self.skipTest("Place creation failed, skipping test_create_review")
        url = f"{BASE_URL}/reviews/"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        data = {
            "place_id": self.place_id,
            "text": "Great place!"
        }
        response = requests.post(url, json=data, headers=headers)
        print("Test Creating a Review:", response.status_code, response.json())
        self.assertEqual(response.status_code, 201, f"Expected 201, got {response.status_code}")
        self.review_id = response.json().get('id')

    def test_update_review(self):
        if not hasattr(self, 'review_id'):
            self.skipTest("Review creation failed, skipping test_update_review")
        url = f"{BASE_URL}/reviews/{self.review_id}"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        data = {
            "text": "Updated review"
        }
        response = requests.put(url, json=data, headers=headers)
        print("Test Updating a Review:", response.status_code, response.json())
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

    def test_delete_review(self):
        if not hasattr(self, 'review_id'):
            self.skipTest("Review creation failed, skipping test_delete_review")
        url = f"{BASE_URL}/reviews/{self.review_id}"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.delete(url, headers=headers)
        print("Test Deleting a Review:", response.status_code)
        self.assertEqual(response.status_code, 204, f"Expected 204, got {response.status_code}")

    def test_modify_user_data(self):
        url = f"{BASE_URL}/users/{self.user_id}"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        data = {
            "first_name": "Updated Name",
            "last_name": "Updated Last Name"
        }
        response = requests.put(url, json=data, headers=headers)
        print("Test Modifying User Data:", response.status_code, response.json())
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

    def test_public_endpoints(self):
        # Retrieve a list of places
        url = f"{BASE_URL}/places/"
        response = requests.get(url)
        print("Retrieve a list of places:", response.status_code, response.json())
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

        # Retrieve detailed information about a specific place
        place_id = "1fa85f64-5717-4562-b3fc-2c963f66afa6"
        url = f"{BASE_URL}/places/{place_id}"
        response = requests.get(url)
        print("Retrieve detailed information about a specific place:", response.status_code, response.json())
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

if __name__ == "__main__":
    unittest.main()
