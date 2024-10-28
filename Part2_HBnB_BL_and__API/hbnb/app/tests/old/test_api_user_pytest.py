#!/usr/bin/python3

#run:  pytest test_api.py
import requests
import pytest

BASE_URL = "http://127.0.0.1:5000/api/v1/users"  # Update with your API's base URL

@pytest.fixture
def setup_user():
    test_user = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com"
    }
    # Create a user to test against
    response = requests.post(BASE_URL, json=test_user)
    user_id = response.json().get("id")
    yield user_id
    requests.delete(f"{BASE_URL}/{user_id}")  # Cleanup after test

def test_create_user():
    test_user = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com"
    }
    response = requests.post(BASE_URL, json=test_user)
    assert response.status_code == 201
    assert "id" in response.json()

def test_get_user_by_id(setup_user):
    response = requests.get(f"{BASE_URL}/{setup_user}")
    assert response.status_code == 200
    assert response.json()["first_name"] == "John"

def test_get_all_users():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_user(setup_user):
    test_user_update = {
        "first_name": "Jane",
        "last_name": "Doe",
        "email": "jane.doe@example.com"
    }
    response = requests.put(f"{BASE_URL}/{setup_user}", json=test_user_update)
    assert response.status_code == 200
    assert response.json()["first_name"] == "Jane"

def test_update_user_not_found():
    test_user_update = {
        "first_name": "Jane",
        "last_name": "Doe",
        "email": "jane.doe@example.com"
    }
    response = requests.put(f"{BASE_URL}/invalid_id", json=test_user_update)
    assert response.status_code == 404
