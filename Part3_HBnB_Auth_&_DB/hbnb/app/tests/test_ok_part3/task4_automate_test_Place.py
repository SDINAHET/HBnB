import requests
import unittest
import csv

BASE_URL = "http://127.0.0.1:5000/api/v1"
ADMIN_CREDENTIALS = {
    "first_name": "Admin",
    "last_name": "User",
    "email": "adminuser@example.com",
    "password": "adminpassword",
    "is_admin": True
}
USER_CREDENTIALS = {
    "first_name": "Regular",
    "last_name": "User",
    "email": "regularuser@example.com",
    "password": "userpassword",
    "is_admin": False
}


class PlaceAPITestCase(unittest.TestCase):
    setup_failed = False

    @classmethod
    def setUpClass(cls):
        try:
            # Create Admin User
            print("Creating Admin User...")
            cls.admin_user_id = cls.create_user(ADMIN_CREDENTIALS)
            print(f"Admin User Created: {cls.user_response.status_code} {cls.user_response.json()}")

            # Authenticate Admin User
            print("Authenticating Admin User...")
            cls.admin_token = cls.authenticate_user(ADMIN_CREDENTIALS)
            print(f"Admin Authentication: {cls.auth_response.status_code} {cls.auth_response.json()}")

            # Create Regular User
            print("Creating Regular User...")
            cls.regular_user_id = cls.create_user(USER_CREDENTIALS)
            print(f"Regular User Created: {cls.user_response.status_code} {cls.user_response.json()}")

            # Authenticate Regular User
            print("Authenticating Regular User...")
            cls.regular_token = cls.authenticate_user(USER_CREDENTIALS)
            print(f"Regular User Authentication: {cls.auth_response.status_code} {cls.auth_response.json()}")

            # Create Amenities
            print("Creating Amenity WiFi...")
            cls.amenity_id_1 = cls.create_amenity("WiFi", cls.admin_token)
            print(f"Amenity WiFi Created: {cls.amenity_response.status_code} {cls.amenity_response.json()}")

            print("Creating Amenity Pool...")
            cls.amenity_id_2 = cls.create_amenity("Pool", cls.admin_token)
            print(f"Amenity Pool Created: {cls.amenity_response.status_code} {cls.amenity_response.json()}")

        except Exception as e:
            print(f"Setup failed: {str(e)}")
            cls.setup_failed = True

    @classmethod
    def tearDownClass(cls):
        if not cls.setup_failed:
            # Store necessary data for further testing if needed
            data_to_store = [
                ["admin_user_id", cls.admin_user_id],
                ["admin_token", cls.admin_token],
                ["regular_user_id", cls.regular_user_id],
                ["regular_token", cls.regular_token],
                ["amenity_id_1", cls.amenity_id_1],
                ["amenity_id_2", cls.amenity_id_2],
            ]
            with open('test_data_PLACE.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data_to_store)
            print("Test data successfully written to test_data_PLACE.csv")

    @staticmethod
    def create_user(credentials):
        url = f"{BASE_URL}/users/users/"
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=credentials, headers=headers)
        PlaceAPITestCase.user_response = response
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        return response.json().get('user_id')

    @staticmethod
    def authenticate_user(credentials):
        url = f"{BASE_URL}/auth/login"
        headers = {"Content-Type": "application/json"}
        data = {
            "email": credentials['email'],
            "password": credentials['password']
        }
        response = requests.post(url, json=data, headers=headers)
        PlaceAPITestCase.auth_response = response
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        return response.json().get('access_token')

    @staticmethod
    def create_amenity(name, token):
        url = f"{BASE_URL}/amenities/"
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        data = {"name": name}
        response = requests.post(url, json=data, headers=headers)
        PlaceAPITestCase.amenity_response = response
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        return response.json().get('amenity_id')

    @unittest.skipIf(setup_failed, "Skipping test due to failed setup.")
    def test_create_place_as_admin(self):
        url = f"{BASE_URL}/places/"
        headers = {
            "Authorization": f"Bearer {self.admin_token}",
            "Content-Type": "application/json"
        }
        data = {
            "title": "Test Place Admin",
            "description": "A wonderful place to stay",
            "price": 150.0,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": self.admin_user_id,
            "amenities": [self.amenity_id_1, self.amenity_id_2]
        }
        response = requests.post(url, json=data, headers=headers)
        print(f"Test Create Place as Admin: {response.status_code}")
        if response.status_code == 201:
            print(response.json())
            self.place_id = response.json().get('id')
        else:
            print(f"Error: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 201)

    @unittest.skipIf(setup_failed, "Skipping test due to failed setup.")
    def test_get_all_places(self):
        url = f"{BASE_URL}/places/"
        headers = {"Authorization": f"Bearer {self.admin_token}"}
        response = requests.get(url, headers=headers)
        print(f"Test Get All Places: {response.status_code}")
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"Error: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)

    @unittest.skipIf(setup_failed, "Skipping test due to failed setup.")
    def test_update_place_as_regular_user_not_owner(self):
        # Attempt to update a place created by the admin user as a regular user
        url = f"{BASE_URL}/places/{self.place_id}"
        headers = {
            "Authorization": f"Bearer {self.regular_token}",
            "Content-Type": "application/json"
        }
        data = {
            "title": "Updated Title by Non-Owner",
            "description": "Trying to update as a non-owner",
            "price": 200.0
        }
        response = requests.put(url, json=data, headers=headers)
        print(f"Test Update Place as Non-Owner: {response.status_code}")
        if response.status_code == 403:
            print(response.json())
        else:
            print(f"Error: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 403)

    @unittest.skipIf(setup_failed, "Skipping test due to failed setup.")
    def test_delete_place_as_regular_user_not_owner(self):
        # Attempt to delete a place created by the admin user as a regular user
        url = f"{BASE_URL}/places/{self.place_id}"
        headers = {
            "Authorization": f"Bearer {self.regular_token}"
        }
        response = requests.delete(url, headers=headers)
        print(f"Test Delete Place as Non-Owner: {response.status_code}")
        if response.status_code == 403:
            print(response.json())
        else:
            print(f"Error: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 403)

if __name__ == "__main__":
    unittest.main()
