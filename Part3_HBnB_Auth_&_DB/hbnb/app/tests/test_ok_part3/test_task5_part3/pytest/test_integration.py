import pytest
import json
from app import create_app, db
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

@pytest.fixture
def client():
    """Fixture for setting up Flask test client"""
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # In-memory DB for testing
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_endpoints(client):
    """Test integration of all endpoints"""

    # 1. Create a user
    user_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "password": "secure_password",
    }
    response = client.post("/api/v1/users", json=user_data)
    assert response.status_code == 201
    user_id = response.get_json()["id"]

    # 2. Login user and get JWT token
    login_data = {"email": "john.doe@example.com", "password": "secure_password"}
    response = client.post("/api/v1/auth/login", json=login_data)
    assert response.status_code == 200
    token = response.get_json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 3. Create a place
    place_data = {
        "title": "Beach House",
        "description": "A beautiful house by the sea.",
        "price": 250.75,
        "latitude": 45.0,
        "longitude": -93.0,
    }
    response = client.post("/api/v1/places", json=place_data, headers=headers)
    assert response.status_code == 201
    place_id = response.get_json()["id"]

    # 4. Add an amenity to the place
    amenity_data = {"name": "WiFi"}
    response = client.post(f"/api/v1/places/{place_id}/amenities", json=amenity_data, headers=headers)
    assert response.status_code == 201
    amenity_id = response.get_json()["id"]

    # 5. Create a review for the place
    review_data = {"text": "Amazing place!", "rating": 5}
    response = client.post(f"/api/v1/places/{place_id}/reviews", json=review_data, headers=headers)
    assert response.status_code == 201
    review_id = response.get_json()["id"]

    # 6. Retrieve all reviews for the place
    response = client.get(f"/api/v1/places/{place_id}/reviews", headers=headers)
    assert response.status_code == 200
    assert len(response.get_json()) == 1

    # 7. Delete the review
    response = client.delete(f"/api/v1/reviews/{review_id}", headers=headers)
    assert response.status_code == 204

    # 8. Delete the place
    response = client.delete(f"/api/v1/places/{place_id}", headers=headers)
    assert response.status_code == 204

    # 9. Delete the user
    response = client.delete(f"/api/v1/users/{user_id}", headers=headers)
    assert response.status_code == 204
