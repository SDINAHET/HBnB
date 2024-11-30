import pytest

# Fixtures for sample data
@pytest.fixture
def sample_user_data():
    return {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "password": "password123"
    }

@pytest.fixture
def sample_admin_token(client):
    response = client.post('/api/v1/auth/login', json={
        "email": "admin@hbnb.io",
        "password": "admin1234"
    })
    return response.json.get("access_token")

@pytest.fixture
def sample_user_token(client, sample_user_data):
    client.post('/api/v1/users', json=sample_user_data)
    response = client.post('/api/v1/auth/login', json={
        "email": sample_user_data["email"],
        "password": sample_user_data["password"]
    })
    return response.json.get("access_token")


# Test creating users
def test_create_user_success(client, sample_user_data):
    """
    Test creating a new user successfully.
    """
    response = client.post('/api/v1/users', json=sample_user_data)
    assert response.status_code == 201
    assert response.json["email"] == sample_user_data["email"]
    assert response.json["first_name"] == sample_user_data["first_name"]
    assert response.json["last_name"] == sample_user_data["last_name"]

def test_create_user_duplicate_email(client, sample_user_data):
    """
    Test creating a user with a duplicate email.
    """
    client.post('/api/v1/users', json=sample_user_data)  # Create the first user
    response = client.post('/api/v1/users', json=sample_user_data)  # Try to create a duplicate
    assert response.status_code == 400
    assert "Email already registered" in response.json["message"]

# Test retrieving all users (Admin only)
def test_get_all_users_as_admin(client, sample_admin_token):
    """
    Test retrieving all users as an admin.
    """
    response = client.get('/api/v1/users', headers={
        "Authorization": f"Bearer {sample_admin_token}"
    })
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_all_users_unauthorized(client, sample_user_token):
    """
    Test retrieving all users without admin privileges.
    """
    response = client.get('/api/v1/users', headers={
        "Authorization": f"Bearer {sample_user_token}"
    })
    assert response.status_code == 403
    assert "Admin privileges required" in response.json["message"]

# Test retrieving a single user by ID
def test_get_user_by_id_success(client, sample_user_data, sample_admin_token):
    """
    Test retrieving a user by ID successfully.
    """
    create_response = client.post('/api/v1/users', json=sample_user_data)
    user_id = create_response.json["id"]

    response = client.get(f'/api/v1/users/{user_id}', headers={
        "Authorization": f"Bearer {sample_admin_token}"
    })
    assert response.status_code == 200
    assert response.json["id"] == user_id

def test_get_user_by_id_not_found(client, sample_admin_token):
    """
    Test retrieving a user by a non-existent ID.
    """
    response = client.get('/api/v1/users/non-existent-id', headers={
        "Authorization": f"Bearer {sample_admin_token}"
    })
    assert response.status_code == 404
    assert "User not found" in response.json["message"]

# Test updating users
def test_update_user_success(client, sample_user_data, sample_user_token):
    """
    Test updating user details successfully.
    """
    create_response = client.post('/api/v1/users', json=sample_user_data)
    user_id = create_response.json["id"]

    update_data = {"first_name": "Jane", "last_name": "Doe"}
    response = client.put(f'/api/v1/users/{user_id}', json=update_data, headers={
        "Authorization": f"Bearer {sample_user_token}"
    })
    assert response.status_code == 200
    assert response.json["first_name"] == "Jane"
    assert response.json["last_name"] == "Doe"

def test_update_user_email_restriction(client, sample_user_data, sample_user_token):
    """
    Test updating email or password (restricted attributes).
    """
    create_response = client.post('/api/v1/users', json=sample_user_data)
    user_id = create_response.json["id"]

    update_data = {"email": "new.email@example.com"}
    response = client.put(f'/api/v1/users/{user_id}', json=update_data, headers={
        "Authorization": f"Bearer {sample_user_token}"
    })
    assert response.status_code == 400
    assert "You cannot modify email or password" in response.json["message"]

# Test deleting users
def test_delete_user_success(client, sample_user_data, sample_admin_token):
    """
    Test deleting a user successfully as an admin.
    """
    create_response = client.post('/api/v1/users', json=sample_user_data)
    user_id = create_response.json["id"]

    response = client.delete(f'/api/v1/users/{user_id}', headers={
        "Authorization": f"Bearer {sample_admin_token}"
    })
    assert response.status_code == 200
    assert "User deleted successfully" in response.json["message"]

def test_delete_user_unauthorized(client, sample_user_data, sample_user_token):
    """
    Test deleting a user without admin privileges.
    """
    create_response = client.post('/api/v1/users', json=sample_user_data)
    user_id = create_response.json["id"]

    response = client.delete(f'/api/v1/users/{user_id}', headers={
        "Authorization": f"Bearer {sample_user_token}"
    })
    assert response.status_code == 403
    assert "Admin privileges required" in response.json["message"]
