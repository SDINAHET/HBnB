import requests
import unittest
import csv

BASE_URL = "http://127.0.0.1:5000/api/v1"
USER_CREDENTIALS = {
    "first_name": "Test",
    "last_name": "User",
    "email": "testuser@example.com",
    "password": "password123",
    "is_admin": False
}

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user_id = cls.create_user()
        cls.token = cls.authenticate_user()
        cls.amenity_id_1 = cls.create_amenity("WiFi")
        cls.amenity_id_2 = cls.create_amenity("Pool")
        cls.place_id = cls.create_place()

    @classmethod
    def tearDownClass(cls):
        # Stocker les données dans un fichier CSV
        data_to_store = [
            ["user_id", cls.user_id],
            ["token", cls.token],
            ["amenity_id_1", cls.amenity_id_1],
            ["amenity_id_2", cls.amenity_id_2],
            ["place_id", cls.place_id],
        ]
        with open('test_data.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data_to_store)
        print("Test data successfully written to test_data.csv")

    @staticmethod
    def create_user():
        url = f"{BASE_URL}/users/"
        response = requests.post(url, json=USER_CREDENTIALS)
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
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        return response.json().get('access_token')

    @classmethod
    def create_amenity(cls, name):
        url = f"{BASE_URL}/amenities/"
        headers = {"Authorization": f"Bearer {cls.token}"}
        data = {"name": name}
        response = requests.post(url, json=data, headers=headers)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        return response.json().get('id')

    @classmethod
    def create_place(cls):
        url = f"{BASE_URL}/places/"
        headers = {"Authorization": f"Bearer {cls.token}"}
        data = {
            "title": "New Place",
            "description": "A nice place",
            "price": 100.0,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": cls.user_id,
            "amenities": [cls.amenity_id_1, cls.amenity_id_2]
        }
        response = requests.post(url, json=data, headers=headers)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        return response.json().get('id')

    def test_place_creation(self):
        url = f"{BASE_URL}/places/"
        headers = {"Authorization": f"Bearer {self.token}"}
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
        self.assertEqual(response.status_code, 201)

    def test_unauthorized_place_update(self):
        url = f"{BASE_URL}/places/{self.place_id}"
        headers = {"Authorization": f"Bearer {self.token}"}
        data = {
            "title": "Updated Place",
            "description": "An updated nice place",
            "price": 150.0
        }
        response = requests.put(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 403)

if __name__ == "__main__":
    unittest.main()
