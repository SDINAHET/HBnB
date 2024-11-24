import pytest
import json
from app import create_app, db
from app.models.amenity import Amenity

@pytest.fixture
def client():
    """Configuration du client Flask pour les tests"""
    app = create_app('testing')
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.session.remove()
            db.drop_all()

def test_create_amenity(client):
    """Test de création d'une nouvelle amenity"""
    amenity_data = {'name': 'WiFi'}
    response = client.post('/api/v1/amenities/',
                           data=json.dumps(amenity_data),
                           content_type='application/json')
    assert response.status_code == 201
    assert 'WiFi' in response.get_data(as_text=True)

def test_get_all_amenities(client):
    """Test pour récupérer toutes les amenities"""
    # Ajouter une amenity
    amenity_data = {'name': 'WiFi'}
    client.post('/api/v1/amenities/',
                data=json.dumps(amenity_data),
                content_type='application/json')

    # Récupérer toutes les amenities
    response = client.get('/api/v1/amenities/')
    assert response.status_code == 200
    assert 'WiFi' in response.get_data(as_text=True)

def test_get_single_amenity(client):
    """Test pour récupérer une amenity par son ID"""
    # Ajouter une amenity
    amenity_data = {'name': 'WiFi'}
    post_response = client.post('/api/v1/amenities/',
                                data=json.dumps(amenity_data),
                                content_type='application/json')
    amenity_id = json.loads(post_response.data)['id']

    # Récupérer l'amenity
    response = client.get(f'/api/v1/amenities/{amenity_id}')
    assert response.status_code == 200
    assert 'WiFi' in response.get_data(as_text=True)

def test_update_amenity(client):
    """Test de mise à jour d'une amenity"""
    # Ajouter une amenity
    amenity_data = {'name': 'WiFi'}
    post_response = client.post('/api/v1/amenities/',
                                data=json.dumps(amenity_data),
                                content_type='application/json')
    amenity_id = json.loads(post_response.data)['id']

    # Mettre à jour l'amenity
    updated_data = {'name': 'Swimming Pool'}
    response = client.put(f'/api/v1/amenities/{amenity_id}',
                          data=json.dumps(updated_data),
                          content_type='application/json')
    assert response.status_code == 200
    assert 'Swimming Pool' in response.get_data(as_text=True)

def test_delete_amenity(client):
    """Test de suppression d'une amenity"""
    # Ajouter une amenity
    amenity_data = {'name': 'WiFi'}
    post_response = client.post('/api/v1/amenities/',
                                data=json.dumps(amenity_data),
                                content_type='application/json')
    amenity_id = json.loads(post_response.data)['id']

    # Supprimer l'amenity
    response = client.delete(f'/api/v1/amenities/{amenity_id}')
    assert response.status_code == 204

    # Vérifier que l'amenity n'existe plus
    response = client.get(f'/api/v1/amenities/{amenity_id}')
    assert response.status_code == 404
