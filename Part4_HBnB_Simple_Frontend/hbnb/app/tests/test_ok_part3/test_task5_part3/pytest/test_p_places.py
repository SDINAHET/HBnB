import pytest
import requests

BASE_URL = "http://127.0.0.1:5000/api/v1"

@pytest.fixture
def headers(user_token):
    """Fixture for authorization headers."""
    return {"Authorization": f"Bearer {user_token}"}


def test_create_place(headers):
    """Test creating a new place."""
    place_data = {
        "title": "Cozy Apartment",
        "description": "A beautiful place to stay.",
        "price": 100.50,
        "latitude": 12.34,
        "longitude": 56.78,
    }
    response = requests.post(f"{BASE_URL}/places/", json=place_data, headers=headers)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["title"] == "Cozy Apartment"
    assert response_data["price"] == 100.50
    assert response_data["latitude"] == 12.34
    assert response_data["longitude"] == 56.78


def test_create_place_invalid_data(headers):
    """Test creating a place with invalid data."""
    invalid_place_data = {
        "title": "",  # Title should not be empty
        "price": -50.0,  # Price should be positive
        "latitude": "invalid_latitude",  # Invalid latitude format
    }
    response = requests.post(f"{BASE_URL}/places/", json=invalid_place_data, headers=headers)
    assert response.status_code == 400
    assert "Validation error" in response.json()["error"]


def test_get_all_places(headers):
    """Test retrieving all places."""
    # Create two places
    place_data_1 = {
        "title": "Place One",
        "price": 150.00,
        "latitude": 10.0,
        "longitude": 20.0,
    }
    place_data_2 = {
        "title": "Place Two",
        "price": 200.00,
        "latitude": 30.0,
        "longitude": 40.0,
    }
    requests.post(f"{BASE_URL}/places/", json=place_data_1, headers=headers)
    requests.post(f"{BASE_URL}/places/", json=place_data_2, headers=headers)

    response = requests.get(f"{BASE_URL}/places/", headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data) >= 2
    assert any(place["title"] == "Place One" for place in response_data)
    assert any(place["title"] == "Place Two" for place in response_data)


def test_get_place_by_id(headers):
    """Test retrieving a single place by ID."""
    place_data = {
        "title": "Test Place",
        "price": 300.00,
        "latitude": 15.0,
        "longitude": 25.0,
    }
    create_response = requests.post(f"{BASE_URL}/places/", json=place_data, headers=headers)
    place_id = create_response.json()["id"]

    response = requests.get(f"{BASE_URL}/places/{place_id}/", headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == place_id
    assert response_data["title"] == "Test Place"
    assert response_data["price"] == 300.00


def test_update_place(headers):
    """Test updating a place."""
    place_data = {
        "title": "Original Place",
        "price": 250.00,
        "latitude": 20.0,
        "longitude": 30.0,
    }
    create_response = requests.post(f"{BASE_URL}/places/", json=place_data, headers=headers)
    place_id = create_response.json()["id"]

    update_data = {
        "title": "Updated Place",
        "price": 275.00,
    }
    response = requests.put(f"{BASE_URL}/places/{place_id}/", json=update_data, headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["title"] == "Updated Place"
    assert response_data["price"] == 275.00


def test_delete_place(headers):
    """Test deleting a place."""
    place_data = {
        "title": "Place to Delete",
        "price": 180.00,
        "latitude": 25.0,
        "longitude": 35.0,
    }
    create_response = requests.post(f"{BASE_URL}/places/", json=place_data, headers=headers)
    place_id = create_response.json()["id"]

    delete_response = requests.delete(f"{BASE_URL}/places/{place_id}/", headers=headers)
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Place deleted successfully."

    # Verify the place no longer exists
    get_response = requests.get(f"{BASE_URL}/places/{place_id}/", headers=headers)
    assert get_response.status_code == 404


def test_cannot_update_other_users_place(headers):
    """Test that a user cannot update a place owned by another user."""
    # Create a place as another user
    other_user_headers = {"Authorization": "Bearer other_user_token"}
    place_data = {
        "title": "Other User's Place",
        "price": 400.00,
        "latitude": 45.0,
        "longitude": 55.0,
    }
    create_response = requests.post(f"{BASE_URL}/places/", json=place_data, headers=other_user_headers)
    place_id = create_response.json()["id"]

    update_data = {"title": "Unauthorized Update"}
    response = requests.put(f"{BASE_URL}/places/{place_id}/", json=update_data, headers=headers)
    assert response.status_code == 403
    assert "Unauthorized action" in response.json()["error"]


def test_create_place_without_auth():
    """Test creating a place without authentication (should fail)."""
    place_data = {
        "title": "Unauthenticated Place",
        "price": 120.00,
        "latitude": 12.0,
        "longitude": 22.0,
    }
    response = requests.post(f"{BASE_URL}/places/", json=place_data)
    assert response.status_code == 401
    assert "Authentication required" in response.json()["error"]
