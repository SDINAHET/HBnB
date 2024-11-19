#!/usr/bin/python3

import unittest
import requests
import time

BASE_URL = "http://localhost:5000/api/v1/places/"

class TestPlaceAPI(unittest.TestCase):

    def get_unique_place_data(self):
        """Génère des données uniques pour créer un nouveau lieu afin d'éviter les doublons."""
        return {
            "title": f"Place-{int(time.time())}",
            "description": "A nice place to stay",
            "price": 100.0,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        }

    def setUp(self):
        """Setup exécuté avant chaque test."""
        self.place_ids_to_cleanup = []

    def tearDown(self):
        """Cleanup exécuté après chaque test pour supprimer les lieux créés."""
        for place_id in self.place_ids_to_cleanup:
            try:
                requests.delete(f"{BASE_URL}{place_id}")
            except Exception as e:
                print(f"Erreur de suppression pour le lieu {place_id}: {e}")

    def test_create_place(self):
        """Test création d'un nouveau lieu."""
        place_data = self.get_unique_place_data()
        response = requests.post(BASE_URL, json=place_data)
        self.assertEqual(response.status_code, 201, "Échec de la création d'un nouveau lieu")

        # Ajouter à la liste des lieux à nettoyer
        data = response.json()
        place_id = data.get("id")
        if place_id:
            self.place_ids_to_cleanup.append(place_id)

        # Vérifier que les données renvoyées sont correctes
        self.assertIn("id", data, "L'ID du lieu devrait être présent dans la réponse")
        self.assertEqual(data["title"], place_data["title"], "Le titre du lieu ne correspond pas")

    def test_create_place_invalid_data(self):
        """Test création d'un lieu avec des données invalides."""
        place_data = {
            "title": "",  # Données invalides : titre vide
            "description": "A nice place to stay",
            "price": -50.0,  # Données invalides : prix négatif
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        }
        response = requests.post(BASE_URL, json=place_data)
        self.assertEqual(response.status_code, 400, "Le serveur devrait renvoyer une erreur 400 pour des données invalides")

    def test_get_all_places(self):
        """Test récupération de tous les lieux."""
        response = requests.get(BASE_URL)
        self.assertEqual(response.status_code, 200, "Échec de la récupération des lieux")

        # Vérifier que la réponse est bien une liste
        data = response.json()
        self.assertIsInstance(data, list, "La réponse devrait être une liste de lieux")

    # def test_get_place_by_id(self):
    #     """Test récupération d'un lieu par ID."""
    #     # Créer un lieu d'abord
    #     place_data = self.get_unique_place_data()
    #     create_response = requests.post(BASE_URL, json=place_data)
    #     self.assertEqual(create_response.status_code, 201, "Échec de la création du lieu")

    #     place_id = create_response.json().get("id")
    #     self.place_ids_to_cleanup.append(place_id)

    #     # Récupérer le lieu créé
    #     response = requests.get(f"{BASE_URL}{place_id}")
    #     self.assertEqual(response.status_code, 200, "Échec de la récupération du lieu")

    #     # Vérifier que les informations sur le lieu sont correctes
    #     data = response.json()
    #     self.assertEqual(data["id"], place_id, "L'ID du lieu ne correspond pas")
    #     self.assertEqual(data["title"], place_data["title"], "Le titre du lieu ne correspond pas")

    def test_get_place_by_id(self):
        """Test récupération d'un lieu par ID, y compris les informations sur le propriétaire et les amenities."""
        # Créer un lieu d'abord
        place_data = self.get_unique_place_data()
        create_response = requests.post(BASE_URL, json=place_data)
        self.assertEqual(create_response.status_code, 201, "Échec de la création du lieu")

        # Extraire l'ID du lieu créé
        place_id = create_response.json().get("id")

        # Récupérer le lieu créé par son ID
        response = requests.get(f"{BASE_URL}{place_id}")
        self.assertEqual(response.status_code, 200, "Échec de la récupération du lieu")

        # Vérifier que les informations renvoyées correspondent aux attentes
        data = response.json()
        self.assertEqual(data["id"], place_id, "L'ID du lieu ne correspond pas")
        self.assertEqual(data["title"], place_data["title"], "Le titre du lieu ne correspond pas")
        self.assertEqual(data["description"], place_data["description"], "La description du lieu ne correspond pas")
        self.assertEqual(data["latitude"], place_data["latitude"], "La latitude du lieu ne correspond pas")
        self.assertEqual(data["longitude"], place_data["longitude"], "La longitude du lieu ne correspond pas")

        # Vérification des informations du propriétaire
        self.assertIn("owner", data, "Les informations du propriétaire doivent être présentes")
        owner_data = data["owner"]
        self.assertIn("id", owner_data, "L'ID du propriétaire doit être présent")
        self.assertIn("first_name", owner_data, "Le prénom du propriétaire doit être présent")
        self.assertIn("last_name", owner_data, "Le nom du propriétaire doit être présent")
        self.assertIn("email", owner_data, "L'email du propriétaire doit être présent")

        # Vérification des informations des amenities
        self.assertIn("amenities", data, "Les amenities doivent être présentes")
        amenities_data = data["amenities"]
        self.assertIsInstance(amenities_data, list, "Les amenities doivent être une liste")
        for amenity in amenities_data:
            self.assertIn("id", amenity, "Chaque amenity doit avoir un ID")
            self.assertIn("name", amenity, "Chaque amenity doit avoir un nom")

    def test_get_place_not_found(self):
        """Test récupération d'un lieu inexistant."""
        response = requests.get(f"{BASE_URL}invalid_id")
        self.assertEqual(response.status_code, 404, "Le serveur devrait renvoyer une erreur 404 pour un lieu non trouvé")

    def test_update_place(self):
        """Test mise à jour des informations d'un lieu."""
        # Créer un lieu d'abord
        place_data = self.get_unique_place_data()
        create_response = requests.post(BASE_URL, json=place_data)
        self.assertEqual(create_response.status_code, 201, "Échec de la création du lieu")

        place_id = create_response.json().get("id")
        self.place_ids_to_cleanup.append(place_id)

        # Mettre à jour le lieu
        update_data = {
            "title": "Luxury Condo",
            "description": "An upscale place to stay",
            "price": 200.0
        }
        response = requests.put(f"{BASE_URL}{place_id}", json=update_data)
        self.assertEqual(response.status_code, 200, "Échec de la mise à jour du lieu")

        # Vérifier que le lieu a bien été mis à jour
        updated_response = requests.get(f"{BASE_URL}{place_id}")
        updated_data = updated_response.json()
        self.assertEqual(updated_data["title"], "Luxury Condo", "Le titre du lieu n'a pas été mis à jour correctement")
        self.assertEqual(updated_data["description"], "An upscale place to stay", "La description du lieu n'a pas été mise à jour correctement")

    def test_update_place_not_found(self):
        """Test mise à jour d'un lieu inexistant."""
        update_data = {
            "title": "Luxury Condo",
            "description": "An upscale place to stay",
            "price": 200.0
        }
        response = requests.put(f"{BASE_URL}invalid_id", json=update_data)
        self.assertEqual(response.status_code, 404, "Le serveur devrait renvoyer une erreur 404 pour un lieu non trouvé")

if __name__ == '__main__':
    unittest.main()
