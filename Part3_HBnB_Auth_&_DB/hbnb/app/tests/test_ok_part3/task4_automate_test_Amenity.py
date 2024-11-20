import unittest
import requests
import csv

BASE_URL = "http://127.0.0.1:5000/api/v1"
ADMIN_CREDENTIALS = {
    "first_name": "Admin",
    "last_name": "User",
    "email": "admin@example.com",
    "password": "adminpassword",
    "is_admin": True
}
NON_ADMIN_CREDENTIALS = {
    "first_name": "Regular",
    "last_name": "User",
    "email": "user@example.com",
    "password": "userpassword",
    "is_admin": False
}

class AmenityAPITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create admin and non-admin users
        cls.admin_user_id, cls.admin_token = cls.create_user(ADMIN_CREDENTIALS)
        cls.non_admin_user_id, cls.non_admin_token = cls.create_user(NON_ADMIN_CREDENTIALS)

        # Create amenities for both admin and non-admin
        cls.amenity_non_admin_1_id = cls.create_amenity(cls.non_admin_token, "NonAdmin Amenity 1", expect_success=False)
        cls.amenity_non_admin_2_id = cls.create_amenity(cls.non_admin_token, "NonAdmin Amenity 2", expect_success=False)
        cls.amenity_admin_1_id = cls.create_amenity(cls.admin_token, "Admin Amenity 1", expect_success=True)
        cls.amenity_admin_2_id = cls.create_amenity(cls.admin_token, "Admin Amenity 2", expect_success=True)

        # Save data to CSV
        data_to_store = [
            ["admin_user_id", cls.admin_user_id],
            ["admin_token", cls.admin_token],
            ["non_admin_user_id", cls.non_admin_user_id],
            ["non_admin_token", cls.non_admin_token],
            ["amenity_non_admin_1_id", cls.amenity_non_admin_1_id],
            ["amenity_non_admin_2_id", cls.amenity_non_admin_2_id],
            ["amenity_admin_1_id", cls.amenity_admin_1_id],
            ["amenity_admin_2_id", cls.amenity_admin_2_id],
        ]
        with open('test_data_Amenity.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data_to_store)
        print("Test data successfully written to test_data_Amenity.csv")

    @staticmethod
    def create_user(credentials):
        url = f"{BASE_URL}/users/users/"
        response = requests.post(url, json=credentials)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        user_id = response.json().get('user_id')

        # Authenticate the user to get token
        auth_url = f"{BASE_URL}/auth/login"
        auth_response = requests.post(auth_url, json={
            "email": credentials['email'],
            "password": credentials['password']
        })
        assert auth_response.status_code == 200, f"Expected 200, got {auth_response.status_code}"
        token = auth_response.json().get('access_token')

        return user_id, token

    @staticmethod
    def create_amenity(token, amenity_name, expect_success=True):
        url = f"{BASE_URL}/amenities/"
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        response = requests.post(url, json={"name": amenity_name}, headers=headers)
        if expect_success:
            assert response.status_code == 201, f"Expected 201, got {response.status_code}"
            return response.json().get('amenity_id')
        else:
            assert response.status_code == 403, f"Expected 403 for non-admin, got {response.status_code}"
            return None

    def test_get_all_amenities_as_admin(self):
        url = f"{BASE_URL}/amenities/admin/"
        headers = {"Authorization": f"Bearer {self.admin_token}"}
        response = requests.get(url, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_get_all_amenities_as_non_admin(self):
        url = f"{BASE_URL}/amenities/admin/"
        headers = {"Authorization": f"Bearer {self.non_admin_token}"}
        response = requests.get(url, headers=headers)
        self.assertEqual(response.status_code, 403)

    def test_update_amenity_as_admin(self):
        url = f"{BASE_URL}/amenities/{self.amenity_admin_1_id}"
        headers = {"Authorization": f"Bearer {self.admin_token}", "Content-Type": "application/json"}
        response = requests.put(url, json={"name": "Updated Admin Amenity"}, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_update_amenity_as_non_admin(self):
        url = f"{BASE_URL}/amenities/{self.amenity_admin_1_id}"
        headers = {"Authorization": f"Bearer {self.non_admin_token}", "Content-Type": "application/json"}
        response = requests.put(url, json={"name": "Attempted Update by Non-Admin"}, headers=headers)
        self.assertEqual(response.status_code, 403)

if __name__ == "__main__":
    unittest.main()
