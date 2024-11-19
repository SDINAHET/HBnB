import requests
import unittest
import json

BASE_URL = "http://127.0.0.1:5000/api/v1"

# Lire les valeurs nécessaires à partir du fichier JSON
with open('test_data.json', 'r') as f:
    test_data = json.load(f)

class APITestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user_id = test_data['user_id']
        cls.token = test_data['token']
        cls.amenity_id_1 = test_data['amenity_id_1']
        cls.amenity_id_2 = test_data['amenity_id_2']
        cls.place_id = test_data['place_id']

    def test_update_place(self):
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
        print("Update Place:", response.status_code, response.json())
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

    def test_create_review(self):
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
        print("Create Review:", response.status_code, response.json())
        self.assertEqual(response.status_code, 201, f"Expected 201, got {response.status_code}")
        self.review_id = response.json().get('id')

    def test_update_review(self):
        self.test_create_review()  # Ensure a review is created first
        url = f"{BASE_URL}/reviews/{self.review_id}"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        data = {
            "text": "Updated review"
        }
        response = requests.put(url, json=data, headers=headers)
        print("Update Review:", response.status_code, response.json())
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

    def test_delete_review(self):
        self.test_create_review()  # Ensure a review is created first
        url = f"{BASE_URL}/reviews/{self.review_id}"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.delete(url, headers=headers)
        print("Delete Review:", response.status_code)
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
        print("Modify User Data:", response.status_code, response.json())
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

    def test_public_endpoints(self):
        # Retrieve a list of places
        url = f"{BASE_URL}/places/"
        response = requests.get(url)
        print("Retrieve a list of places:", response.status_code, response.json())
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

        # Retrieve detailed information about a specific place
        url = f"{BASE_URL}/places/{self.place_id}"
        response = requests.get(url)
        print("Retrieve detailed information about a specific place:", response.status_code, response.json())
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

if __name__ == "__main__":
    unittest.main()
