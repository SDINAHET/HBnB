import pytest
# from hbnb.run import app
from run import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def admin_token(client):
    response = client.post('/api/v1/auth/login', json={
        "email": "admin@hbnb.io",
        "password": "admin1234"
    })
    return response.json["access_token"]

@pytest.fixture
def user_token(client):
    response = client.post('/api/v1/auth/login', json={
        "email": "user@hbnb.io",
        "password": "userpassword"
    })
    return response.json["access_token"]

@pytest.fixture
def user_id():
    return "valid_user_id_here"

@pytest.fixture
def place_id():
    return "valid_place_id_here"

@pytest.fixture
def review_id():
    return "valid_review_id_here"

@pytest.fixture
def amenity_id():
    return "valid_amenity_id_here"
