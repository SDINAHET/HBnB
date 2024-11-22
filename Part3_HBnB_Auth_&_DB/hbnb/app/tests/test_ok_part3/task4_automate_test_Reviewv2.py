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
USER_CREDENTIALS_1 = {
    "first_name": "User1",
    "last_name": "One",
    "email": "user1@example.com",
    "password": "user1password",
    "is_admin": False
}
USER_CREDENTIALS_2 = {
    "first_name": "User2",
    "last_name": "Two",
    "email": "user2@example.com",
    "password": "user2password",
    "is_admin": False
}

class ReviewAPITestCase(unittest.TestCase):
    setup_failed = False

    @classmethod
    def setUpClass(cls):
        try:
            # Create Admin User
            cls.admin_user_id = cls.create_user(ADMIN_CREDENTIALS)
            cls.admin_token = cls.authenticate_user(ADMIN_CREDENTIALS)

            # Create Regular Users
            cls.user1_id = cls.create_user(USER_CREDENTIALS_1)
            cls.user1_token = cls.authenticate_user(USER_CREDENTIALS_1)

            cls.user2_id = cls.create_user(USER_CREDENTIALS_2)
            cls.user2_token = cls.authenticate_user(USER_CREDENTIALS_2)

            # Create Amenities
            cls.amenity_id_1 = cls.create_amenity("WiFi", cls.admin_token)
            cls.amenity_id_2 = cls.create_amenity("Pool", cls.admin_token)

            # Create a Place as User 1 for Reviews
            cls.place_id_user1 = cls.create_place("User1's Place", cls.user1_token, cls.user1_id, [cls.amenity_id_1, cls.amenity_id_2])

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
                ["user1_id", cls.user1_id],
                ["user1_token", cls.user1_token],
                ["user2_id", cls.user2_id],
                ["user2_token", cls.user2_token],
                ["amenity_id_1", cls.amenity_id_1],
                ["amenity_id_2", cls.amenity_id_2],
                ["place_id_user1", cls.place_id_user1],
            ]
            with open('test_data_REVIEW.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data_to_store)
            print("Test data successfully written to test_data_REVIEW.csv")

    @staticmethod
    def create_user(credentials):
        url = f"{BASE_URL}/users/users/"
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=credentials, headers=headers)
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
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        return response.json().get('access_token')

    @staticmethod
    def create_amenity(name, token):
        url = f"{BASE_URL}/amenities/"
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        data = {"name": name}
        response = requests.post(url, json=data, headers=headers)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        return response.json().get('amenity_id')

    @staticmethod
    def create_place(title, token, owner_id, amenities):
        url = f"{BASE_URL}/places/"
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        data = {
            "title": title,
            "description": "A place to review",
            "price": 100.0,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": owner_id,
            "amenities": amenities
        }
        response = requests.post(url, json=data, headers=headers)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        return response.json().get('id')

    @staticmethod
    def create_review(token, text, rating, user_id, place_id):
        url = f"{BASE_URL}/reviews/"
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        data = {
            "text": text,
            "rating": rating,
            "user_id": user_id,
            "place_id": place_id
        }
        response = requests.post(url, json=data, headers=headers)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        return response.json().get('id')

    @unittest.skipIf(setup_failed, "Skipping test due to failed setup.")
    def test_create_review_as_regular_user(self):
        review_id = self.create_review(
            token=self.user2_token,
            text="Great place!",
            rating=5,
            user_id=self.user2_id,
            place_id=self.place_id_user1
        )
        print(f"Review Created: {review_id}")
        self.assertIsNotNone(review_id)

    @unittest.skipIf(setup_failed, "Skipping test due to failed setup.")
    def test_create_duplicate_review_should_fail(self):
        # Create the first review
        self.create_review(
            token=self.user2_token,
            text="Great place!",
            rating=5,
            user_id=self.user2_id,
            place_id=self.place_id_user1
        )
        # Attempt to create a duplicate review
        url = f"{BASE_URL}/reviews/"
        headers = {"Authorization": f"Bearer {self.user2_token}", "Content-Type": "application/json"}
        data = {
            "text": "Another review",
            "rating": 4,
            "user_id": self.user2_id,
            "place_id": self.place_id_user1
        }
        response = requests.post(url, json=data, headers=headers)
        print(f"Test Create Duplicate Review: {response.status_code}, Response: {response.json()}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json().get('message'), "You have already reviewed this place.")

if __name__ == "__main__":
    unittest.main()
