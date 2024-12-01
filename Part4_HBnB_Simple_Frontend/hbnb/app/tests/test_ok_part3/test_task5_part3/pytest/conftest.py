import pytest
import requests

BASE_URL = "http://127.0.0.1:5000/api/v1"

@pytest.fixture
def user_data():
    return {
        "email": "testuser@example.com",
        "password": "password123",
        "first_name": "Test",
        "last_name": "User"
    }

@pytest.fixture
def admin_data():
    return {
        "email": "admin@example.com",
        "password": "admin123",
        "first_name": "Admin",
        "last_name": "User",
        "is_admin": True
    }

@pytest.fixture
def user_token(user_data):
    # Create and login a user to get a token
    requests.post(f"{BASE_URL}/users/", json=user_data)
    response = requests.post(f"{BASE_URL}/auth/login", json={"email": user_data["email"], "password": user_data["password"]})
    return response.json().get("access_token")

@pytest.fixture
def admin_token(admin_data):
    # Create and login an admin to get a token
    requests.post(f"{BASE_URL}/users/", json=admin_data)
    response = requests.post(f"{BASE_URL}/auth/login", json={"email": admin_data["email"], "password": admin_data["password"]})
    return response.json().get("access_token")
