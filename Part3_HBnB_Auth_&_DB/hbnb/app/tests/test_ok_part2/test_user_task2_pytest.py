#!/usr/bin/python3

import requests
import pytest
from app.models.user import User, ValidationError
from datetime import datetime

BASE_URL = "http://localhost:5000/api/v1/users/"  # Remplacez par l'URL de votre API
email_counter = 1  # Compteur global pour les emails uniques

def get_unique_email():
    """Generate a unique email address for testing."""
    global email_counter
    email = f"test_user_{email_counter}@example.com"
    email_counter += 1
    return email

@pytest.fixture
def setup_user():
    """Fixture pour créer un utilisateur par défaut."""
    email = get_unique_email()
    user_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": email
    }
    response = requests.post(BASE_URL, json=user_data)
    user_id = response.json().get("id")
    yield user_id
    requests.delete(f"{BASE_URL}{user_id}")  # Nettoyage après le test

def test_create_user():
    """Test de création d'utilisateur avec gestion des erreurs."""
    # Cas de succès
    user_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": get_unique_email()
    }
    response = requests.post(BASE_URL, json=user_data)
    assert response.status_code == 201
    assert "id" in response.json()

    # Cas d'échec : email déjà enregistré
    response = requests.post(BASE_URL, json=user_data)
    assert response.status_code == 400

    # Cas d'échec : données invalides (email manquant)
    invalid_user_data = {
        "first_name": "Jane",
        "last_name": "Doe"
    }
    response = requests.post(BASE_URL, json=invalid_user_data)
    assert response.status_code == 400

def test_get_user_by_id(setup_user):
    """Test pour récupérer un utilisateur par ID."""
    response = requests.get(f"{BASE_URL}{setup_user}")
    assert response.status_code == 200

def test_list_users():
    """Test pour récupérer la liste des utilisateurs."""
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)

def test_update_user(setup_user):
    """Test de mise à jour d'un utilisateur avec gestion des erreurs."""
    updated_data = {
        "first_name": "Jane",
        "last_name": "Doe",
        "email": get_unique_email()
    }
    response = requests.put(f"{BASE_URL}{setup_user}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["first_name"] == "Jane"
