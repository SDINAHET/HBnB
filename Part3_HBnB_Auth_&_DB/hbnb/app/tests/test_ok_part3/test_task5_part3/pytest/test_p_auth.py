import requests

BASE_URL = "http://127.0.0.1:5000/api/v1"

def test_register_user():
    response = requests.post(f"{BASE_URL}/users/", json={
        "email": "testauth@example.com",
        "password": "password123",
        "first_name": "Auth",
        "last_name": "Test"
    })
    assert response.status_code == 201
    assert response.json()["email"] == "testauth@example.com"

def test_login_user(user_data):
    response = requests.post(f"{BASE_URL}/auth/login", json={
        "email": user_data["email"],
        "password": user_data["password"]
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
