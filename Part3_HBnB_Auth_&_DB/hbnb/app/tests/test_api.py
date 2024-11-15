#!/usr/bin/python3
import requests
import unittest

BASE_URL = "http://127.0.0.1:5000/api/v1"
USER_CREDENTIALS = {
    "first_name": "Test",
    "last_name": "User",
    "email": "testuser@example.com",
    "password": "password123"
}

def create_user():
    url = f"{BASE_URL}/users/"
    response = requests.post(url, json=USER_CREDENTIALS)
    print("Create User:", response.status_code, response.json())
    return response.json().get('id')

def authenticate_user():
    url = f"{BASE_URL}/auth/login"
    data = {
        "email": USER_CREDENTIALS['email'],
        "password": USER_CREDENTIALS['password']
    }
    response = requests.post(url, json=data)
    print("Authenticate User:", response.status_code, response.json())
    return response.json().get('access_token')

def test_place_creation(token):
    url = f"{BASE_URL}/places/"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "title": "New Place",
        "description": "A nice place",
        "price": 100.0,
        "latitude": 37.7749,
        "longitude": -122.4194
    }
    response = requests.post(url, json=data, headers=headers)
    print("Test Place Creation:", response.status_code, response.json())
    return response.json().get('id')

def test_unauthorized_place_update(token, place_id):
    url = f"{BASE_URL}/places/{place_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "title": "Updated Place",
        "description": "An updated nice place",
        "price": 150.0,
        "latitude": 37.7749,
        "longitude": -122.4194
    }
    response = requests.put(url, json=data, headers=headers)
    print("Test Unauthorized Place Update:", response.status_code, response.json())

def test_create_review(token, place_id):
    url = f"{BASE_URL}/reviews/"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "place_id": place_id,
        "text": "Great place!"
    }
    response = requests.post(url, json=data, headers=headers)
    print("Test Creating a Review:", response.status_code, response.json())
    return response.json().get('id')

def test_update_review(token, review_id):
    url = f"{BASE_URL}/reviews/{review_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "text": "Updated review"
    }
    response = requests.put(url, json=data, headers=headers)
    print("Test Updating a Review:", response.status_code, response.json())

def test_delete_review(token, review_id):
    url = f"{BASE_URL}/reviews/{review_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.delete(url, headers=headers)
    print("Test Deleting a Review:", response.status_code, response.json())

def test_modify_user_data(token, user_id):
    url = f"{BASE_URL}/users/{user_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "first_name": "Updated Name",
        "last_name": "Updated Last Name"
    }
    response = requests.put(url, json=data, headers=headers)
    print("Test Modifying User Data:", response.status_code, response.json())

def test_public_endpoints():
    # Retrieve a list of places
    url = f"{BASE_URL}/places/"
    response = requests.get(url)
    print("Retrieve a list of places:", response.status_code, response.json())

    # Retrieve detailed information about a specific place
    place_id = "1fa85f64-5717-4562-b3fc-2c963f66afa6"
    url = f"{BASE_URL}/places/{place_id}"
    response = requests.get(url)
    print("Retrieve detailed information about a specific place:", response.status_code, response.json())

if __name__ == "__main__":
    user_id = create_user()
    token = authenticate_user()
    place_id = test_place_creation(token)
    test_unauthorized_place_update(token, place_id)
    review_id = test_create_review(token, place_id)
    test_update_review(token, review_id)
    test_delete_review(token, review_id)
    test_modify_user_data(token, user_id)
    test_public_endpoints()
