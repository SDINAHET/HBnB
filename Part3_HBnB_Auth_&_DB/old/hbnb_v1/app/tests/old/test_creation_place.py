import unittest
import subprocess
import json

from app.models.base_entity import ValidationError
from app.models.user import User
from app.models.place import Place
from app.models.amenity import Amenity

class TestCreatePlace(unittest.TestCase):
    BASE_URL = 'http://localhost:5000/api/v1'

    def setUp(self):
        # Création d'un utilisateur et d'une amenity pour le test
        self.user_id = self.create_user("Test", "User", "testuser@example.com", False)
        self.amenity_id = self.create_amenity("Wifi")

    def tearDown(self):
        # Suppression de l'utilisateur et de l'amenity si nécessaire
        self.delete_user(self.user_id)
        self.delete_amenity(self.amenity_id)

    def create_user(self, first_name, last_name, email, is_admin):
        """ Crée un utilisateur et retourne son ID. """
        command = f"curl -X 'POST' '{self.BASE_URL}/users/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{{\"first_name\": \"{first_name}\", \"last_name\": \"{last_name}\", \"email\": \"{email}\", \"is_admin\": {str(is_admin).lower()}}}'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        user_data = json.loads(result.stdout)
        return user_data['id']

    def create_amenity(self, name):
        """ Crée une amenity et retourne son ID. """
        command = f"curl -X 'POST' '{self.BASE_URL}/amenities/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{{\"name\": \"{name}\"}}'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        amenity_data = json.loads(result.stdout)
        return amenity_data['id']

    def create_place(self, title, description, price, latitude, longitude, owner_id, amenities):
        """ Crée une place et retourne sa réponse. """
        command = f"curl -X 'POST' '{self.BASE_URL}/places/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{{\"title\": \"{title}\", \"description\": \"{description}\", \"price\": {price}, \"latitude\": {latitude}, \"longitude\": {longitude}, \"owner_id\": \"{owner_id}\", \"amenities\": {json.dumps(amenities)}}}'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return json.loads(result.stdout)

    def delete_user(self, user_id):
        """ Supprime un utilisateur donné par son ID. """
        command = f"curl -X 'DELETE' '{self.BASE_URL}/users/{user_id}'"
        subprocess.run(command, shell=True)

    def delete_amenity(self, amenity_id):
        """ Supprime une amenity donnée par son ID. """
        command = f"curl -X 'DELETE' '{self.BASE_URL}/amenities/{amenity_id}'"
        subprocess.run(command, shell=True)

    def test_create_place(self):
        """ Test pour créer une place. """
        place_response = self.create_place(
            title="Maison Rennes",
            description="Un joli chalet",
            price=120,
            latitude=41.0,
            longitude=52.3,
            owner_id=self.user_id,
            amenities=[self.amenity_id]
        )

        self.assertIsNotNone(place_response)  # Vérifiez que la réponse n'est pas None
        if place_response:  # S'assurer que nous avons une réponse
            self.assertEqual(place_response.get('title'), "Maison Rennes")
            self.assertEqual(place_response.get('price'), 120)

if __name__ == '__main__':
    unittest.main()
