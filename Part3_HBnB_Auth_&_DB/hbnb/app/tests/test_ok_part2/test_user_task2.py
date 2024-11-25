#!/usr/bin/python3

# python3 -m unittest app.tests.test_user_task2

import sys
import os
import time
import unittest
import requests  # Ajout de l'import manquant
from datetime import datetime
from app.models.user import User, ValidationError
import logging

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
        # """Generate a unique email address for testing."""
        # timestamp = int(time.time())
        # email = f"test_user_{timestamp}@example.com"
        # return email

    def setUp(self):
        """Create a default user for tests."""
        self.default_email = self.get_unique_email()
        self.user = User(first_name="John", last_name="Doe", email=self.default_email)

    # Test avec toute les sorties d'erreur possible pour l'USER
    def test_create_user(self):
        """Test successful user creation and error handling."""
        # Cas de succès
        user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com"
        }
        response = requests.post(BASE_URL, json=user_data)
        self.assertEqual(response.status_code, 201, f"Expected 201, got {response.status_code}")
        self.assertIn("id", response.json(), "User ID not found in response")

        # Cas d'échec : email déjà enregistré
        response = requests.post(BASE_URL, json=user_data)
        self.assertEqual(response.status_code, 400, f"Expected 400, got {response.status_code}")
        print(f"Error message: {response.json().get('error')}")  # Affichage du message d'erreur

        # Cas d'échec : données invalides (email manquant)
        invalid_user_data = {
            "first_name": "Jane",
            "last_name": "Doe"
        }
        response = requests.post(BASE_URL, json=invalid_user_data)
        self.assertEqual(response.status_code, 400, f"Expected 400, got {response.status_code}")
        print(f"Error message: {response.json().get('error')}")  # Affichage du message d'erreur

    def test_get_user_by_id(self):
        # """Test retrieving a user by ID and handle errors."""
        # user_id = "3fa85f64-5717-4562-b3fc-2c963f66afa6"

        # # Cas de succès
        # response = requests.get(f"{BASE_URL}{user_id}")
        # self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

        # # Cas d'échec : utilisateur non trouvé
        # response = requests.get(f"{BASE_URL}nonexistent_id")
        # self.assertEqual(response.status_code, 404, f"Expected 404, got {response.status_code}")
        # print(f"Error message: {response.json().get('error')}")  # Affichage du message d'erreur
        """Test retrieving a user by ID and handle errors."""
        # Créer un utilisateur avant de tester la récupération par ID
        user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example2.com"
        }
        create_response = requests.post(BASE_URL, json=user_data)
        user_id = create_response.json().get("id")

        # Maintenant, testez la récupération par ID
        response = requests.get(f"{BASE_URL}{user_id}")
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

        # Cleanup: delete the user after the test
        # requests.delete(f"{BASE_URL}{user_id}")

    def test_list_users(self):
        """Test retrieving the list of users."""
        response = requests.get(BASE_URL)
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")
        users = response.json()
        self.assertIsInstance(users, list, "Expected a list of users")

    def test_update_user(self):
        """Test updating a user and handle errors."""
        # Create a user for testing
        user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": self.get_unique_email()
        }
        create_response = requests.post(BASE_URL, json=user_data)
        self.assertEqual(create_response.status_code, 201, "Failed to create user")
        print(f"Create response: {create_response.json()}")  # Debugging

        user_id = create_response.json().get("id")

        # Now test updating this user
        updated_data = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
            # "email": self.get_unique_email()
        }
         # Updated URL to include user_id in the path
        response = requests.put(f"{BASE_URL}{user_id}", json=updated_data)
        print(f"Update response: {response.json()}")  # Add more detailed debug output
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")
        # print(response.json())  # Print the JSON response for debugging
        print(f"Update response: {response.json()}")  # Debugging output

        # Cleanup: delete the user after the test
        # requests.delete(f"{BASE_URL}{user_id}")
        # delete_response = requests.delete(f"{BASE_URL}{user_id}")
        # self.assertEqual(delete_response.status_code, 204, "Failed to delete user after test")

if __name__ == "__main__":
    unittest.main()
