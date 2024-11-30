import pytest

def test_register_user_success(client):
    """
    Test registering a new user successfully.
    """
    response = client.post('/api/v1/auth/register', json={
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com",
        "password": "password123"
    })
    assert response.status_code == 201
    assert "id" in response.json
    assert response.json["email"] == "johndoe@example.com"

def test_register_user_duplicate_email(client):
    """
    Test registering a user with an email that already exists.
    """
    client.post('/api/v1/auth/register', json={
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com",
        "password": "password123"
    })
    response = client.post('/api/v1/auth/register', json={
        "first_name": "Jane",
        "last_name": "Doe",
        "email": "johndoe@example.com",
        "password": "anotherpassword"
    })
    assert response.status_code == 400
    assert "Email already exists" in response.json["message"]

def test_login_success(client, registered_user):
    """
    Test login with valid credentials.
    """
    response = client.post('/api/v1/auth/login', json={
        "email": registered_user["email"],
        "password": registered_user["password"]
    })
    assert response.status_code == 200
    assert "access_token" in response.json

def test_login_invalid_password(client, registered_user):
    """
    Test login with an invalid password.
    """
    response = client.post('/api/v1/auth/login', json={
        "email": registered_user["email"],
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    assert response.json["message"] == "Invalid credentials"

def test_login_unregistered_email(client):
    """
    Test login with an email that is not registered.
    """
    response = client.post('/api/v1/auth/login', json={
        "email": "nonexistent@example.com",
        "password": "password123"
    })
    assert response.status_code == 404
    assert response.json["message"] == "User not found"

def test_get_current_user_success(client, access_token):
    """
    Test retrieving the current logged-in user's details.
    """
    response = client.get('/api/v1/auth/me', headers={
        "Authorization": f"Bearer {access_token}"
    })
    assert response.status_code == 200
    assert "email" in response.json
    assert response.json["email"] == "johndoe@example.com"

def test_get_current_user_unauthorized(client):
    """
    Test retrieving current user without a valid token.
    """
    response = client.get('/api/v1/auth/me')
    assert response.status_code == 401
    assert response.json["message"] == "Missing or invalid token"

def test_refresh_token_success(client, refresh_token):
    """
    Test refreshing an access token using a valid refresh token.
    """
    response = client.post('/api/v1/auth/refresh', headers={
        "Authorization": f"Bearer {refresh_token}"
    })
    assert response.status_code == 200
    assert "access_token" in response.json

def test_refresh_token_invalid(client):
    """
    Test refreshing an access token with an invalid token.
    """
    response = client.post('/api/v1/auth/refresh', headers={
        "Authorization": "Bearer invalidtoken"
    })
    assert response.status_code == 401
    assert response.json["message"] == "Invalid token"

def test_logout_success(client, access_token):
    """
    Test logging out by invalidating the access token.
    """
    response = client.post('/api/v1/auth/logout', headers={
        "Authorization": f"Bearer {access_token}"
    })
    assert response.status_code == 200
    assert response.json["message"] == "Successfully logged out"

def test_logout_unauthorized(client):
    """
    Test logging out without a valid token.
    """
    response = client.post('/api/v1/auth/logout')
    assert response.status_code == 401
    assert response.json["message"] == "Missing or invalid token"
