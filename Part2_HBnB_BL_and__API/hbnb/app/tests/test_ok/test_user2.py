#!/usr/bin/python3

import sys
import os
import unittest
import requests  # Ajout de l'import manquant
from datetime import datetime
from app.models.user import User, ValidationError

BASE_URL = "http://localhost:5000/api/v1/users/"  # Remplacez par l'URL de votre API

# Append the project's root directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestUser(unittest.TestCase):
    email_counter = 1

    def get_unique_email(self):
        """Generate a unique email address for testing."""
        email = f"test_user_{TestUser.email_counter}@example.com"
        TestUser.email_counter += 1
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

    def test_user_invalid_email(self):
        """Test user creation with an invalid email."""
        with self.assertRaises(ValidationError):
            User(first_name="Jane", last_name="Doe", email="invalidemail")

    def test_user_missing_first_name(self):
        """Test user creation with a missing first name."""
        with self.assertRaises(ValidationError):
            User(first_name="", last_name="Doe", email=self.get_unique_email())

    def test_user_missing_last_name(self):
        """Test user creation with a missing last name."""
        with self.assertRaises(ValidationError):
            User(first_name="Jane", last_name="", email=self.get_unique_email())

    def test_user_unique_email(self):
        """Test that email must be unique."""
        User(first_name="John", last_name="Doe", email=self.get_unique_email())
        with self.assertRaises(ValidationError):
            User(first_name="Jane", last_name="Smith", email=self.user.email)

    def test_user_first_name_length(self):
        """Test user creation with a first name exceeding maximum length."""
        with self.assertRaises(ValidationError):
            User(first_name="A" * 51, last_name="Doe", email=self.get_unique_email())

    def test_user_last_name_length(self):
        """Test user creation with a last name exceeding maximum length."""
        with self.assertRaises(ValidationError):
            User(first_name="John", last_name="D" * 51, email=self.get_unique_email())

    def test_user_id_type(self):
        """Test that the user id is of the correct type."""
        self.assertIsInstance(self.user.id, str)

    def test_user_is_admin_default(self):
        """Test that the default value for is_admin is False."""
        self.assertFalse(self.user.is_admin)

    def test_user_update(self):
        """Test updating user information and ensuring updated_at changes."""
        old_updated_at = self.user.updated_at
        # Pause to ensure timestamp difference
        self.user.first_name = "Jane"
        self.user.last_name = "Smith"
        self.user.email = self.get_unique_email()

        # Assuming your User model has a method to save the updated user
        self.user.save()

        # Check if the values have been updated
        self.assertEqual(self.user.first_name, "Jane")
        self.assertEqual(self.user.last_name, "Smith")
        self.assertNotEqual(self.user.email, self.default_email)

        # Check if updated_at has changed
        self.assertGreater(self.user.updated_at, old_updated_at)


    # # Test avec toute les sorties d'erreur possible pour l'USER
    # def test_create_user(self):
    #     """Test successful user creation and error handling."""
    #     # Cas de succès
    #     user_data = {
    #         "first_name": "John",
    #         "last_name": "Doe",
    #         "email": "john.doe@example.com"
    #     }
    #     response = requests.post(BASE_URL, json=user_data)
    #     self.assertEqual(response.status_code, 201, f"Expected 201, got {response.status_code}")
    #     self.assertIn("id", response.json(), "User ID not found in response")

    #     # Cas d'échec : email déjà enregistré
    #     response = requests.post(BASE_URL, json=user_data)
    #     self.assertEqual(response.status_code, 400, f"Expected 400, got {response.status_code}")
    #     print(f"Error message: {response.json().get('error')}")  # Affichage du message d'erreur

    #     # Cas d'échec : données invalides (email manquant)
    #     invalid_user_data = {
    #         "first_name": "Jane",
    #         "last_name": "Doe"
    #     }
    #     response = requests.post(BASE_URL, json=invalid_user_data)
    #     self.assertEqual(response.status_code, 400, f"Expected 400, got {response.status_code}")
    #     print(f"Error message: {response.json().get('error')}")  # Affichage du message d'erreur

    # def test_get_user_by_id(self):
    #     # """Test retrieving a user by ID and handle errors."""
    #     # user_id = "3fa85f64-5717-4562-b3fc-2c963f66afa6"

    #     # # Cas de succès
    #     # response = requests.get(f"{BASE_URL}{user_id}")
    #     # self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

    #     # # Cas d'échec : utilisateur non trouvé
    #     # response = requests.get(f"{BASE_URL}nonexistent_id")
    #     # self.assertEqual(response.status_code, 404, f"Expected 404, got {response.status_code}")
    #     # print(f"Error message: {response.json().get('error')}")  # Affichage du message d'erreur
    #     """Test retrieving a user by ID and handle errors."""
    #     # Créer un utilisateur avant de tester la récupération par ID
    #     user_data = {
    #         "first_name": "John",
    #         "last_name": "Doe",
    #         "email": "john.doe@example.com"
    #     }
    #     create_response = requests.post(BASE_URL, json=user_data)
    #     user_id = create_response.json().get("id")

    #     # Maintenant, testez la récupération par ID
    #     response = requests.get(f"{BASE_URL}{user_id}")
    #     self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

    # def test_list_users(self):
    #     """Test retrieving the list of users."""
    #     response = requests.get(BASE_URL)
    #     self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")
    #     users = response.json()
    #     self.assertIsInstance(users, list, "Expected a list of users")

    # def test_update_user(self):
    #     # """Test updating a user and handle errors."""
    #     # user_id = "3eb1e3bf-6d66-4279-9b82-b102975f5a59"

    #     # # Cas de succès
    #     # updated_data = {
    #     #     "first_name": "Jane",
    #     #     "last_name": "Doe",
    #     #     "email": "jane.doe@example.com"
    #     # }
    #     # response = requests.put(f"{BASE_URL}{user_id}", json=updated_data)
    #     # self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

    #     # # Cas d'échec : utilisateur non trouvé
    #     # response = requests.put(f"{BASE_URL}nonexistent_id", json=updated_data)
    #     # self.assertEqual(response.status_code, 404, f"Expected 404, got {response.status_code}")
    #     # print(f"Error message: {response.json().get('error')}")  # Affichage du message d'erreur

    #     # # Cas d'échec : données invalides
    #     # invalid_data = {
    #     #     "first_name": "",
    #     #     "last_name": "Doe",
    #     #     "email": "invalid_email_format"
    #     # }
    #     # response = requests.put(f"{BASE_URL}{user_id}", json=invalid_data)
    #     # self.assertEqual(response.status_code, 400, f"Expected 400, got {response.status_code}")
    #     # print(f"Error message: {response.json().get('error')}")  # Affichage du message d'erreur
    #     """Test updating a user and handle errors."""
    #     # Créer un utilisateur pour pouvoir le mettre à jour
    #     user_data = {
    #         "first_name": "John",
    #         "last_name": "Doe",
    #         "email": "john.doe@example.com"
    #     }
    #     create_response = requests.post(BASE_URL, json=user_data)
    #     self.assertEqual(create_response.status_code, 201, "Failed to create user")

    #     user_id = create_response.json().get("id")

    #     # Maintenant, testez la mise à jour de cet utilisateur
    #     updated_data = {
    #         "first_name": "Jane",
    #         "last_name": "Doe",
    #         "email": "jane.doe@example.com"
    #     }
    #     response = requests.put(f"{BASE_URL}{user_id}", json=updated_data)
    #     self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")
    #     print(response.json())  # Affiche le corps de la réponse JSON

if __name__ == "__main__":
    unittest.main()
