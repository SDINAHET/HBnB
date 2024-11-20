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
        print("Creating Admin User...")
        cls.user_id = cls.create_user()
        print(f"Create User: {cls.user_response.status_code} {cls.user_response.json()}")

        print("Authenticating User...")
        cls.token = cls.authenticate_user()
        print(f"Authenticate User: {cls.auth_response.status_code} {cls.auth_response.json()}")

    @classmethod
    def tearDownClass(cls):
        data_to_store = [
            ["user_id", cls.user_id],
            ["token", cls.token],
        ]
        with open('test_data_USER.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data_to_store)
        print("Test data successfully written to test_data_USER.csv")

    @staticmethod
    def create_user():
        url = f"{BASE_URL}/admin/users/"
        response = requests.post(url, json=USER_CREDENTIALS)
        APITestCase.user_response = response
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        return response.json().get('user_id')

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

    def test_create_user(self):
        url = f"{BASE_URL}/users/"
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@example.com",
            "password": "password123"
        }
        response = requests.post(url, json=data)
        print(f"Test Create User: {response.status_code} {response.json()}")
        self.assertEqual(response.status_code, 201)

    def test_get_user_by_id(self):
        url = f"{BASE_URL}/users/{self.user_id}"
        response = requests.get(url)
        print(f"Test Get User by ID: {response.status_code} {response.json()}")
        self.assertEqual(response.status_code, 200)

    def test_get_user_by_email(self):
        url = f"{BASE_URL}/users/email/{USER_CREDENTIALS['email']}"
        response = requests.get(url)
        print(f"Test Get User by Email: {response.status_code} {response.json()}")
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        url = f"{BASE_URL}/users/{self.user_id}"
        headers = {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}
        data = {
            "first_name": "UpdatedName",
            "last_name": "UpdatedLastName"
        }
        response = requests.put(url, json=data, headers=headers)
        print(f"Test Update User: {response.status_code} {response.json()}")
        self.assertEqual(response.status_code, 200)

    def test_get_all_users_admin(self):
        url = f"{BASE_URL}/admin/users"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=headers)
        print(f"Test Get All Users (Admin): {response.status_code} {response.json()}")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
