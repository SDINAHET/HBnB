import pytest

# Fixtures for sample data
@pytest.fixture
def sample_amenity_data():
    return {"name": "Swimming Pool"}

@pytest.fixture
def sample_admin_token(client):
    response = client.post('/api/v1/auth/login', json={
        "email": "admin@hbnb.io",
        "password": "admin1234"
    })
    return response.json.get("access_token")

@pytest.fixture
def sample_user_token(client):
    response = client.post('/api/v1/auth/login', json={
        "email": "john.doe@example.com",
        "password": "password123"
    })
    return response.json.get("access_token")


# Test creating amenities
def test_create_amenity_success(client, sample_amenity_data, sample_admin_token):
    """
    Test creating a new amenity successfully as an admin.
    """
    response = client.post('/api/v1/amenities', json=sample_amenity_data, headers={
        "Authorization": f"Bearer {sample_admin_token}"
    })
    assert response.status_code == 201
    assert response.json["name"] == sample_amenity_data["name"]

def test_create_amenity_unauthorized(client, sample_amenity_data, sample_user_token):
    """
    Test creating an amenity without admin privileges.
    """
    response = client.post('/api/v1/amenities', json=sample_amenity_data, headers={
        "Authorization": f"Bearer {sample_user_token}"
    })
    assert response.status_code == 403
    assert "Admin privileges required" in response.json["message"]

def test_create_amenity_duplicate_name(client, sample_amenity_data, sample_admin_token):
    """
    Test creating an amenity with a duplicate name.
    """
    client.post('/api/v1/amenities', json=sample_amenity_data, headers={
        "Authorization": f"Bearer {sample_admin_token}"
    })
    response = client.post('/api/v1/amenities', json=sample_amenity_data, headers={
        "Authorization": f"Bearer {sample_admin_token}"
    })
    assert response.status_code == 400
    assert "Amenity already exists" in response.json["message"]

# Test retrieving all amenities
def test_get_all_amenities(client, sample_admin_token):
    """
    Test retrieving all amenities.
    """
    response = client.get('/api/v1/amenities', headers={
        "Authorization": f"Bearer {sample_admin_token}"
    })
    assert response.status_code == 200
    assert isinstance(response.json, list)

# Test retrieving a specific amenity by ID
def test_get_amenity_by_id_success(client, sample_amenity_data, sample_admin_token):
    """
    Test retrieving an amenity by its ID successfully.
    """
    create_response = client.post('/api/v1/amenities', json=sample_amenity_data, headers={
        "Authorization": f"Bearer {sample_admin_token}"
    })
    amenity_id = create_response.json["id"]

    response = client.get(f'/api/v1/amenities/{amenity_id}', headers={
        "Authorization": f"Bearer {sample_admin_token}"
    })
    assert response.status_code == 200
    assert response.json["id"] == amenity_id

def test_get_amenity_by_id_not_found(client, sample_admin_token):
    """
    Test retrieving an amenity with a non-existent ID.
    """
    response = client.get('/api/v1/amenities/non-existent-id', headers={
        "Authorization": f"Bearer {sample_admin_token}"
    })
    assert response.status_code == 404
    assert "Amenity not found" in response.json["message"]

# Test updating amenities
def test_update_amenity_success(client, sample_amenity_data, sample_admin_token):
    """
    Test updating an amenity successfully.
    """
    create_response = client.post('/api/v1/amenities', json=sample_amenity_data, headers={
        "Authorization": f"Bearer {sample_admin_token}"
    })
    amenity_id = create_response.json["id"]

    update_data = {"name": "Updated Amenity"}
    response = client.put(f'/api/v1/amenities/{amenity_id}', json=update_data, headers={
        "Authorization": f"Bearer {sample_admin_token}"
    })
    assert response.status_code == 200
    assert response.json["name"] == "Updated Amenity"

def test_update_amenity_unauthorized(client, sample_amenity_data, sample_user_token):
    """
    Test updating an amenity without admin privileges.
    """
    create_response = client.post('/api/v1/amenities', json=sample_amenity_data, headers={
        "Authorization": f"Bearer {sample_user_token}"
    })
    amenity_id = create_response.json["id"]

    update_data = {"name": "New Name"}
    response = client.put(f'/api/v1/amenities/{amenity_id}', json=update_data, headers={
        "Authorization": f"Bearer {sample_user_token}"
    })
    assert response.status_code == 403
    assert "Admin privileges required" in response.json["message"]

# Test deleting amenities
def test_delete_amenity_success(client, sample_amenity_data, sample_admin_token):
    """
    Test deleting an amenity successfully as an admin.
    """
    create_response = client.post('/api/v1/amenities', json=sample_amenity_data, headers={
        "Authorization": f"Bearer {sample_admin_token}"
    })
    amenity_id = create_response.json["id"]

    response = client.delete(f'/api/v1/amenities/{amenity_id}', headers={
        "Authorization": f"Bearer {sample_admin_token}"
    })
    assert response.status_code == 200
    assert "Amenity deleted successfully" in response.json["message"]

def test_delete_amenity_unauthorized(client, sample_amenity_data, sample_user_token):
    """
    Test deleting an amenity without admin privileges.
    """
    create_response = client.post('/api/v1/amenities', json=sample_amenity_data, headers={
        "Authorization": f"Bearer {sample_user_token}"
    })
    amenity_id = create_response.json["id"]

    response = client.delete(f'/api/v1/amenities/{amenity_id}', headers={
        "Authorization": f"Bearer {sample_user_token}"
    })
    assert response.status_code == 403
    assert "Admin privileges required" in response.json["message"]

    # hbnb/app/tests/test_amenities.py

def test_update_amenity_success(client, sample_amenity_data, sample_admin_token):
    """
    Test updating an amenity successfully.
    """
    create_response = client.post('/api/v1/amenities', json=sample_amenity_data, headers={
        "Authorization": f"Bearer {sample_admin_token}"
    })
    amenity_id = create_response.json["id"]

    update_data = {"name": "Updated Amenity"}
    response = client.put(f'/api/v1/amenities/{amenity_id}', json=update_data, headers={
        "Authorization": f"Bearer {sample_admin_token}"
    })
    assert response.status_code == 200
    assert response.json["name"] == "Updated Amenity"

def test_update_amenity_not_found(client, sample_admin_token):
    """
    Test updating a non-existent amenity.
    """
    update_data = {"name": "Non-existent"}
    response = client.put('/api/v1/amenities/non-existent-id', json=update_data, headers={
        "Authorization": f"Bearer {sample_admin_token}"
    })
    assert response.status_code == 404
    assert "Amenity not found" in response.json["message"]

def test_update_amenity_unauthorized(client, sample_amenity_data, sample_user_token):
    """
    Test updating an amenity without admin privileges.
    """
    create_response = client.post('/api/v1/amenities', json=sample_amenity_data, headers={
        "Authorization": f"Bearer {sample_user_token}"
    })
    amenity_id = create_response.json["id"]

    update_data = {"name": "Unauthorized Update"}
    response = client.put(f'/api/v1/amenities/{amenity_id}', json=update_data, headers={
        "Authorization": f"Bearer {sample_user_token}"
    })
    assert response.status_code == 403
    assert "Admin privileges required" in response.json["message"]
