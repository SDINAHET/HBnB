import unittest
from flask_jwt_extended import create_access_token
from app import create_app, db
from app.models.user import User
from app.models.place import Place


class TestPlaceEndpoints(unittest.TestCase):
    """Test class for Place-related endpoints"""

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

    def test_create_place(self):
        """Test creating a new place"""
        token = self.get_token("testuser@example.com", "password123")
        response = self.client.post(
            "/api/v1/places/",
            json={
                "title": "Cozy Cabin",
                "description": "A warm and cozy cabin in the woods",
                "price": 150.00,
                "latitude": 34.0522,
                "longitude": -118.2437
            },
            headers={"Authorization": f"Bearer {token}"}
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("Cozy Cabin", response.get_json()["title"])

    def test_create_place_without_authentication(self):
        """Test creating a place without authentication"""
        response = self.client.post(
            "/api/v1/places/",
            json={
                "title": "Unauthorized Place",
                "description": "This should not be created",
                "price": 200.00,
                "latitude": 0.0,
                "longitude": 0.0
            }
        )
        self.assertEqual(response.status_code, 401)
        self.assertIn("Missing Authorization Header", response.get_json()["msg"])

    def test_get_place_by_id(self):
        """Test retrieving a place by ID"""
        response = self.client.get(f"/api/v1/places/{self.place.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["title"], "Beautiful Apartment")

    def test_update_place(self):
        """Test updating a place"""
        token = self.get_token("testuser@example.com", "password123")
        response = self.client.put(
            f"/api/v1/places/{self.place.id}",
            json={"title": "Updated Apartment"},
            headers={"Authorization": f"Bearer {token}"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["title"], "Updated Apartment")

    def test_update_place_unauthorized(self):
        """Test updating a place by a different user"""
        token = self.get_token("adminuser@example.com", "adminpassword")
        response = self.client.put(
            f"/api/v1/places/{self.place.id}",
            json={"title": "Should Not Update"},
            headers={"Authorization": f"Bearer {token}"}
        )
        self.assertEqual(response.status_code, 403)
        self.assertIn("Unauthorized action", response.get_json()["error"])

    def test_delete_place(self):
        """Test deleting a place"""
        token = self.get_token("testuser@example.com", "password123")
        response = self.client.delete(
            f"/api/v1/places/{self.place.id}",
            headers={"Authorization": f"Bearer {token}"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("Place deleted successfully", response.get_json()["message"])

    def test_delete_place_unauthorized(self):
        """Test deleting a place by a different user"""
        token = self.get_token("adminuser@example.com", "adminpassword")
        response = self.client.delete(
            f"/api/v1/places/{self.place.id}",
            headers={"Authorization": f"Bearer {token}"}
        )
        self.assertEqual(response.status_code, 403)
        self.assertIn("Unauthorized action", response.get_json()["error"])

    def test_get_all_places(self):
        """Test retrieving all places"""
        response = self.client.get("/api/v1/places/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.get_json()) > 0)

if __name__ == "__main__":
    unittest.main()
