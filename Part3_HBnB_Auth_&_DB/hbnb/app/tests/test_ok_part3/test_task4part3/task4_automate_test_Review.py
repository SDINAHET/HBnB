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

class ReviewAPITestCase(unittest.TestCase):
    setup_failed = False

    @classmethod
    def setUpClass(cls):
        try:
            # Create Admin User
            cls.admin_user_id = cls.create_user(ADMIN_CREDENTIALS)
            cls.admin_token = cls.authenticate_user(ADMIN_CREDENTIALS)

            # Create Regular User
            cls.regular_user_id = cls.create_user(USER_CREDENTIALS)
            cls.regular_token = cls.authenticate_user(USER_CREDENTIALS)

            # Create a Place as Admin for Reviews
            cls.place_id = cls.create_place("Test Place for Review", cls.admin_token, cls.admin_user_id)

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
                ["place_id", cls.place_id],
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
    def create_place(title, token, owner_id):
        url = f"{BASE_URL}/places/"
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        data = {
            "title": title,
            "description": "A place to review",
            "price": 100.0,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": owner_id,
            "amenities": []
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
            token=self.regular_token,
            text="Great place!",
            rating=5,
            user_id=self.regular_user_id,
            place_id=self.place_id
        )
        print(f"Review Created: {review_id}")
        self.assertIsNotNone(review_id)

    @unittest.skipIf(setup_failed, "Skipping test due to failed setup.")
    def test_get_all_reviews(self):
        url = f"{BASE_URL}/reviews/"
        headers = {"Authorization": f"Bearer {self.admin_token}"}
        response = requests.get(url, headers=headers)
        print(f"Test Get All Reviews: {response.status_code}, Response: {response.json()}")
        self.assertEqual(response.status_code, 200)

    @unittest.skipIf(setup_failed, "Skipping test due to failed setup.")
    def test_get_reviews_for_place(self):
        url = f"{BASE_URL}/places/{self.place_id}/reviews"
        headers = {"Authorization": f"Bearer {self.admin_token}"}
        response = requests.get(url, headers=headers)
        print(f"Test Get Reviews for Place: {response.status_code}")
        self.assertEqual(response.status_code, 200)

    @unittest.skipIf(setup_failed, "Skipping test due to failed setup.")
    def test_update_review_as_owner(self):
        review_id = self.create_review(
            token=self.regular_token,
            text="Nice place!",
            rating=4,
            user_id=self.regular_user_id,
            place_id=self.place_id
        )
        url = f"{BASE_URL}/reviews/{review_id}"
        headers = {"Authorization": f"Bearer {self.regular_token}", "Content-Type": "application/json"}
        data = {
            "text": "Updated review text",
            "rating": 3
        }
        response = requests.put(url, json=data, headers=headers)
        print(f"Test Update Review as Owner: {response.status_code}")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
