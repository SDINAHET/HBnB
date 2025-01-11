import unittest
import json
from app import create_app, db
from app.models.amenity import Amenity

class AmenityTestCase(unittest.TestCase):
    """Classe pour tester les fonctionnalités des endpoints Amenity"""

    def setUp(self):
        """Configuration avant chaque test"""
        self.app = create_app('testing')
        self.client = self.app.test_client
        self.headers = {'Content-Type': 'application/json'}
        self.amenity_data = {'name': 'WiFi'}

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """Nettoyage après chaque test"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_amenity(self):
        """Test de création d'une nouvelle amenity"""
        response = self.client().post('/api/v1/amenities/',
                                      data=json.dumps(self.amenity_data),
                                      headers=self.headers)
        self.assertEqual(response.status_code, 201)
        self.assertIn('WiFi', str(response.data))

    def test_get_all_amenities(self):
        """Test pour récupérer toutes les amenities"""
        # Créer une amenity pour le test
        self.client().post('/api/v1/amenities/',
                           data=json.dumps(self.amenity_data),
                           headers=self.headers)

        response = self.client().get('/api/v1/amenities/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('WiFi', str(response.data))

    def test_get_single_amenity(self):
        """Test pour récupérer une amenity par son ID"""
        # Créer une amenity pour le test
        response = self.client().post('/api/v1/amenities/',
                                      data=json.dumps(self.amenity_data),
                                      headers=self.headers)
        amenity_id = json.loads(response.data)['id']

        # Récupérer cette amenity par son ID
        response = self.client().get(f'/api/v1/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('WiFi', str(response.data))

    def test_update_amenity(self):
        """Test de mise à jour d'une amenity"""
        # Créer une amenity pour le test
        response = self.client().post('/api/v1/amenities/',
                                      data=json.dumps(self.amenity_data),
                                      headers=self.headers)
        amenity_id = json.loads(response.data)['id']

        # Mettre à jour cette amenity
        updated_data = {'name': 'Swimming Pool'}
        response = self.client().put(f'/api/v1/amenities/{amenity_id}',
                                     data=json.dumps(updated_data),
                                     headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Swimming Pool', str(response.data))

    def test_delete_amenity(self):
        """Test de suppression d'une amenity"""
        # Créer une amenity pour le test
        response = self.client().post('/api/v1/amenities/',
                                      data=json.dumps(self.amenity_data),
                                      headers=self.headers)
        amenity_id = json.loads(response.data)['id']

        # Supprimer cette amenity
        response = self.client().delete(f'/api/v1/amenities/{amenity_id}',
                                        headers=self.headers)
        self.assertEqual(response.status_code, 204)

        # Vérifier qu'elle n'existe plus
        response = self.client().get(f'/api/v1/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
