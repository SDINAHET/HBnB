import unittest
from flask_jwt_extended import create_access_token
from app import create_app, db
from app.models.user import User

class TestAuthEndpoints(unittest.TestCase):
    """Test class for the authentication endpoints"""

    def setUp(self):
        """Set up the test environment"""
        self.app = create_app("config.TestingConfig")
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

            # Create a test user
            user = User(
                first_name="Test",
                last_name="User",
                email="testuser@example.com",
                password="hashed_password",
                is_admin=False
            )
            user.hash_password("password123")
            db.session.add(user)
            db.session.commit()

    def tearDown(self):
        """Tear down the test environment"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_login_success(self):
        """Test successful login with valid credentials"""
        response = self.client.post(
            "/api/v1/auth/login",
            json={"email": "testuser@example.com", "password": "password123"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.get_json())

    def test_login_invalid_credentials(self):
        """Test login with invalid credentials"""
        response = self.client.post(
            "/api/v1/auth/login",
            json={"email": "testuser@example.com", "password": "wrong_password"}
        )
        self.assertEqual(response.status_code, 401)
        self.assertIn("error", response.get_json())

    def test_protected_endpoint_without_token(self):
        """Test access to a protected endpoint without a token"""
        response = self.client.get("/api/v1/protected")
        self.assertEqual(response.status_code, 401)
        self.assertIn("msg", response.get_json())

    def test_protected_endpoint_with_valid_token(self):
        """Test access to a protected endpoint with a valid token"""
        with self.app.app_context():
            access_token = create_access_token(identity={"id": "1", "is_admin": False})

        response = self.client.get(
            "/api/v1/protected",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.get_json())

if __name__ == "__main__":
    unittest.main()
