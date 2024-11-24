import unittest
import requests  # Ajout de l'import manquant
from datetime import datetime
from app.models.user import User, ValidationError

class TestUserModel(unittest.TestCase):
    email_counter = 1

    def get_unique_email(self):
        """Generate a unique email address for testing."""
        email = f"test_user_{TestUserModel.email_counter}@example.com"
        TestUserModel.email_counter += 1
        return email

    def setUp(self):
        """Create a default user for tests."""
        self.default_email = self.get_unique_email()
        self.user = User(first_name="John", last_name="Doe", email=self.default_email)

    def test_user_creation(self):
        """Test successful user creation."""
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.email, self.default_email)
        self.assertFalse(self.user.is_admin)  # Default value
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)
        print("User creation test passed!")

if __name__ == "__main__":
    unittest.main()
