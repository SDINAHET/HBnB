import pytest
import requests

BASE_URL = "http://127.0.0.1:5000/api/v1"

@pytest.fixture
def headers(user_token):
    """Fixture for authorization headers."""
    return {"Authorization": f"Bearer {user_token}"}


def test_get_user_details(headers):
    """Test retrieving the details of the current user."""
    response = requests.get(f"{BASE_URL}/users/me", headers=headers)
    assert response.status_code == 200
    assert "email" in response.json()
    assert "first_name" in response.json()
    assert "last_name" in response.json()


def test_update_user_details(headers):
    """Test updating the current user's details."""
    response = requests.put(f"{BASE_URL}/users/me", json={"first_name": "UpdatedName"}, headers=headers)
    assert response.status_code == 200
    assert response.json()["first_name"] == "UpdatedName"


def test_cannot_update_email_or_password(headers):
    """Test that the user cannot update their email or password."""
    response = requests.put(f"{BASE_URL}/users/me", json={"email": "newemail@example.com", "password": "newpassword"}, headers=headers)
    assert response.status_code == 400
    assert response.json()["error"] == "You cannot modify email or password."


def test_get_all_users_as_admin(admin_token):
    """Test retrieving all users as an administrator."""
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = requests.get(f"{BASE_URL}/users/", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_non_admin_cannot_get_all_users(headers):
    """Test that a regular user cannot retrieve all users."""
    response = requests.get(f"{BASE_URL}/users/")
    assert response.status_code == 403
    assert response.json()["error"] == "Admin privileges required."


def test_delete_user_as_admin(admin_token):
    """Test deleting a user as an administrator."""
    headers = {"Authorization": f"Bearer {admin_token}"}
    user_to_delete = {
        "email": "delete_me@example.com",
        "password": "password123",
        "first_name": "Delete",
        "last_name": "Me"
    }
    # Create user to delete
    requests.post(f"{BASE_URL}/users/", json=user_to_delete)

    # Get the user's ID
    users_response = requests.get(f"{BASE_URL}/users/", headers=headers)
    user_id = next(user["id"] for user in users_response.json() if user["email"] == user_to_delete["email"])

    # Delete the user
    delete_response = requests.delete(f"{BASE_URL}/users/{user_id}", headers=headers)
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "User deleted successfully."


def test_regular_user_cannot_delete_users(headers):
    """Test that a regular user cannot delete other users."""
    response = requests.delete(f"{BASE_URL}/users/nonexistent_id", headers=headers)
    assert response.status_code == 403
    assert response.json()["error"] == "Admin privileges required."


def test_create_user_with_invalid_email():
    """Test creating a user with an invalid email format."""
    invalid_user_data = {
        "email": "invalidemail",
        "password": "password123",
        "first_name": "Invalid",
        "last_name": "User"
    }
    response = requests.post(f"{BASE_URL}/users/", json=invalid_user_data)
    assert response.status_code == 400
    assert "Invalid email format" in response.json()["error"]


def test_create_user_with_missing_fields():
    """Test creating a user with missing required fields."""
    incomplete_user_data = {
        "email": "missingfields@example.com"
    }
    response = requests.post(f"{BASE_URL}/users/", json=incomplete_user_data)
    assert response.status_code == 400
    assert "Missing required fields" in response.json()["error"]


def test_cannot_create_duplicate_email_user():
    """Test creating a user with an already existing email."""
    duplicate_user_data = {
        "email": "duplicate@example.com",
        "password": "password123",
        "first_name": "Duplicate",
        "last_name": "User"
    }
    # Create the first user
    requests.post(f"{BASE_URL}/users/", json=duplicate_user_data)

    # Attempt to create the duplicate user
    response = requests.post(f"{BASE_URL}/users/", json=duplicate_user_data)
    assert response.status_code == 400
    assert "Email already registered" in response.json()["error"]
