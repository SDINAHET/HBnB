import pytest

# Fixtures for a sample place and owner
@pytest.fixture
def sample_place_data():
    return {
        "title": "Cozy Apartment",
        "description": "A comfortable and affordable place to stay.",
        "price": 120.50,
        "latitude": 48.8566,
        "longitude": 2.3522,
        "owner_id": "36c9050e-ddd3-4c3b-9731-9f487208bbc1"
    }

@pytest.fixture
def sample_owner_token(client):
    response = client.post('/api/v1/auth/login', json={
        "email": "admin@hbnb.io",
        "password": "admin1234"
    })
    return response.json.get("access_token")

def test_create_place_success(client, sample_place_data, sample_owner_token):
    """
    Test creating a new place with valid data.
    """
    response = client.post('/api/v1/places', json=sample_place_data, headers={
        "Authorization": f"Bearer {sample_owner_token}"
    })
    assert response.status_code == 201
    assert response.json["title"] == sample_place_data["title"]
    assert response.json["owner_id"] == sample_place_data["owner_id"]

def test_create_place_unauthorized(client, sample_place_data):
    """
    Test creating a place without authorization.
    """
    response = client.post('/api/v1/places', json=sample_place_data)
    assert response.status_code == 401
    assert "Missing or invalid token" in response.json["message"]

def test_get_places_success(client):
    """
    Test retrieving all places.
    """
    response = client.get('/api/v1/places')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_place_by_id_success(client, sample_place_data, sample_owner_token):
    """
    Test retrieving a single place by its ID.
    """
    # Create a new place
    create_response = client.post('/api/v1/places', json=sample_place_data, headers={
        "Authorization": f"Bearer {sample_owner_token}"
    })
    place_id = create_response.json["id"]

    # Retrieve the created place by ID
    response = client.get(f'/api/v1/places/{place_id}')
    assert response.status_code == 200
    assert response.json["title"] == sample_place_data["title"]

def test_get_place_by_id_not_found(client):
    """
    Test retrieving a place by a non-existent ID.
    """
    response = client.get('/api/v1/places/non-existent-id')
    assert response.status_code == 404
    assert "Place not found" in response.json["message"]

def test_update_place_success(client, sample_place_data, sample_owner_token):
    """
    Test updating a place's information successfully.
    """
    # Create a place
    create_response = client.post('/api/v1/places', json=sample_place_data, headers={
        "Authorization": f"Bearer {sample_owner_token}"
    })
    place_id = create_response.json["id"]

    # Update the place
    update_data = {"title": "Updated Title"}
    response = client.put(f'/api/v1/places/{place_id}', json=update_data, headers={
        "Authorization": f"Bearer {sample_owner_token}"
    })
    assert response.status_code == 200
    assert response.json["title"] == "Updated Title"

def test_update_place_unauthorized(client, sample_place_data):
    """
    Test updating a place without authorization.
    """
    response = client.put('/api/v1/places/non-existent-id', json={"title": "Unauthorized Update"})
    assert response.status_code == 401
    assert "Missing or invalid token" in response.json["message"]

def test_delete_place_success(client, sample_place_data, sample_owner_token):
    """
    Test deleting a place successfully.
    """
    # Create a place
    create_response = client.post('/api/v1/places', json=sample_place_data, headers={
        "Authorization": f"Bearer {sample_owner_token}"
    })
    place_id = create_response.json["id"]

    # Delete the place
    response = client.delete(f'/api/v1/places/{place_id}', headers={
        "Authorization": f"Bearer {sample_owner_token}"
    })
    assert response.status_code == 200
    assert "Place deleted successfully" in response.json["message"]

def test_delete_place_unauthorized(client):
    """
    Test deleting a place without authorization.
    """
    response = client.delete('/api/v1/places/non-existent-id')
    assert response.status_code == 401
    assert "Missing or invalid token" in response.json["message"]

def test_delete_place_not_found(client, sample_owner_token):
    """
    Test deleting a place that does not exist.
    """
    response = client.delete('/api/v1/places/non-existent-id', headers={
        "Authorization": f"Bearer {sample_owner_token}"
    })
    assert response.status_code == 404
    assert "Place not found" in response.json["message"]
