import unittest
from app.models.user import User
from app.persistence.repository import InMemoryRepository

class TestUserModel(unittest.TestCase):
    def setUp(self):
        self.user_repo = InMemoryRepository()
        self.user = User(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            password="password123"
        )
        self.user_repo.add(self.user)

    def test_user_creation(self):
        self.assertIsNotNone(self.user.id)
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.email, "john.doe@example.com")
        self.assertNotEqual(self.user.password, "password123")  # Ensuring password is hashed

    def test_user_retrieval(self):
        retrieved_user = self.user_repo.get(self.user.id)
        self.assertEqual(retrieved_user.email, "john.doe@example.com")

    def test_user_update(self):
        self.user_repo.update(self.user.id, {"first_name": "Jane"})
        updated_user = self.user_repo.get(self.user.id)
        self.assertEqual(updated_user.first_name, "Jane")

if __name__ == "__main__":
    unittest.main()
