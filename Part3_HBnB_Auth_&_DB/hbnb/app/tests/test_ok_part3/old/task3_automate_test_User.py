import requests
import unittest
import csv

BASE_URL = "http://127.0.0.1:5000/api/v1"
USER_CREDENTIALS = {
    "first_name": "Test",
    "last_name": "User",
    "email": "testuser@example.com",
    "password": "password123",
    "is_admin": True
}

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Creating User...")
        cls.user_id = cls.create_user()
        print(f"Create User: {cls.user_response.status_code} {cls.user_response.json()}")

        print("Authenticating User...")
        cls.token = cls.authenticate_user()
        print(f"Authenticate User: {cls.auth_response.status_code} {cls.auth_response.json()}")

        print("Creating Amenity WiFi...")
        cls.amenity_id_1 = cls.create_amenity("WiFi")
        print(f"Create Amenity (WiFi): {cls.amenity_response.status_code} {cls.amenity_response.json()}")

        print("Creating Amenity Pool...")
        cls.amenity_id_2 = cls.create_amenity("Pool")
        print(f"Create Amenity (Pool): {cls.amenity_response.status_code} {cls.amenity_response.json()}")

        print("Creating Place...")
        cls.place_id = cls.create_place()
        print(f"Create Place: {cls.place_response.status_code} {cls.place_response.json()}")

    @classmethod
    def tearDownClass(cls):
        data_to_store = [
            ["user_id", cls.user_id],
            ["token", cls.token],
            ["amenity_id_1", cls.amenity_id_1],
            ["amenity_id_2", cls.amenity_id_2],
            ["place_id", cls.place_id],
        ]
        with open('test_data_USER.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data_to_store)
        print("Test data successfully written to test_data.csv")

    @staticmethod
    def create_user():
        url = f"{BASE_URL}/users/"
        response = requests.post(url, json=USER_CREDENTIALS)
        APITestCase.user_response = response
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
        APITestCase.auth_response = response
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        return response.json().get('access_token')

    @classmethod
    def create_amenity(cls, name):
        url = f"{BASE_URL}/amenities/"
        headers = {"Authorization": f"Bearer {cls.token}"}
        data = {"name": name}
        response = requests.post(url, json=data, headers=headers)
        cls.amenity_response = response
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
        cls.place_response = response
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
        print(f"Test Place Creation: {response.status_code}")
        print(response.json())
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
        print(f"Test Unauthorized Place Update: {response.status_code} {response.json()}")
        self.assertEqual(response.status_code, 403)

    def test_get_all_users(self):
        url = f"{BASE_URL}/users/"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=headers)
        print(f"Test Get All Users: {response.status_code}")
        print(response.json())
        self.assertEqual(response.status_code, 200)

    def test_get_user_by_id(self):
        url = f"{BASE_URL}/users/{self.user_id}"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=headers)
        print(f"Test Get User by ID: {response.status_code}")
        print(response.json())
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        url = f"{BASE_URL}/users/{self.user_id}"
        headers = {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}
        data = {
            "first_name": "UpdatedName",
            "last_name": "UpdatedLastName",
            "email": USER_CREDENTIALS['email'],  # Inclure l'email
            "password": USER_CREDENTIALS['password']  # Inclure le mot de passe
        }
        response = requests.put(url, json=data, headers=headers)
        print(f"Test Update User: {response.status_code}")
        print(response.json())
        self.assertEqual(response.status_code, 200)

        print(""" TEST USER PART3
██╗  ██╗██████╗ ███╗   ██╗██████╗
██║  ██║██╔══██╗████╗  ██║██╔══██╗
███████║███████║██╔██╗ ██║███████║
██╔══██║██║  ██║██║╚██╗██║██║  ██║
██║  ██║██████╔╝██║ ╚████║██████╔╝
╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═══╝╚═════╝
 | HBnB part3 Logo  # C24
""")

if __name__ == "__main__":
    unittest.main()

print("""
██╗  ██╗██████╗ ███╗   ██╗██████╗
██║  ██║██╔══██╗████╗  ██║██╔══██╗
███████║███████║██╔██╗ ██║███████║
██╔══██║██║  ██║██║╚██╗██║██║  ██║
██║  ██║██████╔╝██║ ╚████║██████╔╝
╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═══╝╚═════╝
 | HBnB part3 Logo  # C24
""")
