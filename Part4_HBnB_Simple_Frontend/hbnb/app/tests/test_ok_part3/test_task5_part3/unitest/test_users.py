import unittest
from flask_jwt_extended import create_access_token
from app import create_app, db
from app.models.user import User


class TestUserEndpoints(unittest.TestCase):
    """Test class for user-related endpoints"""

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

    def test_get_user_by_id(self):
        """Test retrieving a user by ID"""
        token = self.get_token("adminuser@example.com", "adminpassword")
        response = self.client.get(
            f"/api/v1/users/{self.user.id}",
            headers={"Authorization": f"Bearer {token}"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["email"], "testuser@example.com")

    def test_update_user_self(self):
        """Test updating user details for the authenticated user"""
        token = self.get_token("testuser@example.com", "password123")
        response = self.client.put(
            f"/api/v1/users/{self.user.id}",
            json={"first_name": "Updated", "last_name": "User"},
            headers={"Authorization": f"Bearer {token}"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["first_name"], "Updated")

    def test_update_user_admin(self):
        """Test an admin updating another user's details"""
        token = self.get_token("adminuser@example.com", "adminpassword")
        response = self.client.put(
            f"/api/v1/users/{self.user.id}",
            json={"first_name": "Admin Updated", "last_name": "User"},
            headers={"Authorization": f"Bearer {token}"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["first_name"], "Admin Updated")

    def test_update_user_invalid(self):
        """Test updating a user with invalid fields"""
        token = self.get_token("testuser@example.com", "password123")
        response = self.client.put(
            f"/api/v1/users/{self.user.id}",
            json={"email": "newemail@example.com"},  # Email update not allowed
            headers={"Authorization": f"Bearer {token}"}
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("You cannot modify email or password", response.get_json()["error"])

    def test_get_users_list_admin(self):
        """Test retrieving the list of all users as an admin"""
        token = self.get_token("adminuser@example.com", "adminpassword")
        response = self.client.get(
            "/api/v1/users/",
            headers={"Authorization": f"Bearer {token}"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.get_json()) > 1)

    def test_get_users_list_non_admin(self):
        """Test that non-admin users cannot retrieve the user list"""
        token = self.get_token("testuser@example.com", "password123")
        response = self.client.get(
            "/api/v1/users/",
            headers={"Authorization": f"Bearer {token}"}
        )
        self.assertEqual(response.status_code, 403)
        self.assertIn("Admin privileges required", response.get_json()["error"])

if __name__ == "__main__":
    unittest.main()
