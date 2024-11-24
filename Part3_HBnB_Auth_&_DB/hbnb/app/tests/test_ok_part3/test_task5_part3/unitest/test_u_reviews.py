import unittest
from flask_jwt_extended import create_access_token
from app import create_app, db
from app.models.user import User
from app.models.place import Place
from app.models.review import Review


class TestReviewEndpoints(unittest.TestCase):
    """Test class for Review-related endpoints"""

    def setUp(self):
        """Set up the test environment"""
        self.app = create_app("config.TestingConfig")
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

            # Create a regular user
            self.user = User(
                first_name="Test",
                last_name="User",
                email="testuser@example.com",
                password="hashed_password",
                is_admin=False
            )
            self.user.hash_password("password123")
            db.session.add(self.user)

            # Create an admin user
            self.admin_user = User(
                first_name="Admin",
                last_name="User",
                email="adminuser@example.com",
                password="hashed_password",
                is_admin=True
            )
            self.admin_user.hash_password("adminpassword")
            db.session.add(self.admin_user)

            # Create a test place
            self.place = Place(
                title="Beautiful Apartment",
                description="A lovely apartment with a great view",
                price=100.00,
                latitude=40.7128,
                longitude=-74.0060,
                owner_id=self.user.id
            )
            db.session.add(self.place)
            db.session.commit()

            # Create a review for the test place
            self.review = Review(
                text="Amazing place to stay!",
                rating=5,
                user_id=self.user.id,
                place_id=self.place.id
            )
            db.session.add(self.review)
            db.session.commit()

    def tearDown(self):
        """Tear down the test environment"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def get_token(self, email, password):
        """Helper function to get a JWT token for a user"""
        response = self.client.post(
            "/api/v1/auth/login",
            json={"email": email, "password": password}
        )
        return response.get_json().get("access_token")

    def test_create_review(self):
        """Test creating a new review"""
        token = self.get_token("testuser@example.com", "password123")
        response = self.client.post(
            "/api/v1/reviews/",
            json={
                "text": "Great service and friendly staff!",
                "rating": 4,
                "place_id": self.place.id
            },
            headers={"Authorization": f"Bearer {token}"}
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("Great service and friendly staff!", response.get_json()["text"])

    def test_create_review_unauthorized(self):
        """Test creating a review without authentication"""
        response = self.client.post(
            "/api/v1/reviews/",
            json={
                "text": "Unauthorized review attempt",
                "rating": 3,
                "place_id": self.place.id
            }
        )
        self.assertEqual(response.status_code, 401)
        self.assertIn("Missing Authorization Header", response.get_json()["msg"])

    def test_create_duplicate_review(self):
        """Test creating a duplicate review for the same place by the same user"""
        token = self.get_token("testuser@example.com", "password123")
        response = self.client.post(
            "/api/v1/reviews/",
            json={
                "text": "Another review for the same place",
                "rating": 4,
                "place_id": self.place.id
            },
            headers={"Authorization": f"Bearer {token}"}
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("You have already reviewed this place", response.get_json()["error"])

    def test_get_review_by_id(self):
        """Test retrieving a review by ID"""
        response = self.client.get(f"/api/v1/reviews/{self.review.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["text"], "Amazing place to stay!")

    def test_update_review(self):
        """Test updating a review"""
        token = self.get_token("testuser@example.com", "password123")
        response = self.client.put(
            f"/api/v1/reviews/{self.review.id}",
            json={"text": "Updated review text", "rating": 5},
            headers={"Authorization": f"Bearer {token}"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["text"], "Updated review text")

    def test_update_review_unauthorized(self):
        """Test updating a review by a different user"""
        token = self.get_token("adminuser@example.com", "adminpassword")
        response = self.client.put(
            f"/api/v1/reviews/{self.review.id}",
            json={"text": "This should not work", "rating": 1},
            headers={"Authorization": f"Bearer {token}"}
        )
        self.assertEqual(response.status_code, 403)
        self.assertIn("Unauthorized action", response.get_json()["error"])

    def test_delete_review(self):
        """Test deleting a review"""
        token = self.get_token("testuser@example.com", "password123")
        response = self.client.delete(
            f"/api/v1/reviews/{self.review.id}",
            headers={"Authorization": f"Bearer {token}"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("Review deleted successfully", response.get_json()["message"])

    def test_delete_review_unauthorized(self):
        """Test deleting a review by a different user"""
        token = self.get_token("adminuser@example.com", "adminpassword")
        response = self.client.delete(
            f"/api/v1/reviews/{self.review.id}",
            headers={"Authorization": f"Bearer {token}"}
        )
        self.assertEqual(response.status_code, 403)
        self.assertIn("Unauthorized action", response.get_json()["error"])

    def test_get_all_reviews(self):
        """Test retrieving all reviews"""
        response = self.client.get("/api/v1/reviews/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.get_json()) > 0)

if __name__ == "__main__":
    unittest.main()
