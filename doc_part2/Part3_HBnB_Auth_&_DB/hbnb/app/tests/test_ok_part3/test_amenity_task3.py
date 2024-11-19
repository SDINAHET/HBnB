#!/usr/bin/python3

import unittest
import requests
import json

BASE_URL = "http://localhost:5000/api/v1/amenities/"  # Remplacez par votre URL API

class TestAmenityAPI(unittest.TestCase):

    def get_unique_name(self):
        """Génère un nom d'amenity unique pour éviter les doublons."""
        return "Wi-Fi-" + str(int(time.time()))

    def test_create_amenity(self):
        """Test création d'une nouvelle amenity."""
        amenity_data = {
            "name": "Wi-Fi"
        }
        response = requests.post(BASE_URL, json=amenity_data)
        self.assertEqual(response.status_code, 201, "Échec de la création d'une nouvelle amenity")

        # Vérifier que les données renvoyées sont correctes
        data = response.json()
        self.assertIn("id", data, "L'ID de l'amenity devrait être présent dans la réponse")
        self.assertEqual(data["name"], "Wi-Fi", "Le nom de l'amenity ne correspond pas")

    def test_create_amenity_invalid_data(self):
        """Test création d'une amenity avec données invalides."""
        amenity_data = {
            "name": ""  # Données invalides : nom vide
        }
        response = requests.post(BASE_URL, json=amenity_data)
        self.assertEqual(response.status_code, 400, "Le serveur devrait renvoyer une erreur 400 pour les données invalides")

    def test_get_all_amenities(self):
        """Test récupération de la liste des amenities."""
        response = requests.get(BASE_URL)
        self.assertEqual(response.status_code, 200, "Échec de la récupération des amenities")

        # Vérifier que la réponse est bien une liste
        data = response.json()
        self.assertIsInstance(data, list, "La réponse devrait être une liste")

    def test_get_amenity_by_id(self):
        """Test récupération d'une amenity par ID."""
        # Créer d'abord une amenity pour le test
        amenity_data = {
            "name": "Wi-Fi"
        }
        create_response = requests.post(BASE_URL, json=amenity_data)
        self.assertEqual(create_response.status_code, 201, "Échec de la création de l'amenity")

        amenity_id = create_response.json().get("id")

        # Récupérer cette amenity
        response = requests.get(f"{BASE_URL}{amenity_id}")
        self.assertEqual(response.status_code, 200, "Échec de la récupération de l'amenity")

        # Vérifier que l'amenity renvoyée est correcte
        data = response.json()
        self.assertEqual(data["id"], amenity_id, "L'ID de l'amenity ne correspond pas")
        self.assertEqual(data["name"], "Wi-Fi", "Le nom de l'amenity ne correspond pas")

    def test_get_amenity_not_found(self):
        """Test récupération d'une amenity non existante."""
        response = requests.get(f"{BASE_URL}invalid_id")
        self.assertEqual(response.status_code, 404, "Le serveur devrait renvoyer une erreur 404 pour une amenity non trouvée")

    def test_update_amenity(self):
        """Test mise à jour des informations d'une amenity."""
        # Créer d'abord une amenity pour le test
        amenity_data = {
            "name": "Wi-Fi"
        }
        create_response = requests.post(BASE_URL, json=amenity_data)
        self.assertEqual(create_response.status_code, 201, "Échec de la création de l'amenity")

        amenity_id = create_response.json().get("id")

        # Mise à jour de cette amenity
        update_data = {
            "name": "Air Conditioning"
        }
        response = requests.put(f"{BASE_URL}{amenity_id}", json=update_data)
        self.assertEqual(response.status_code, 200, "Échec de la mise à jour de l'amenity")

        # Vérifier que l'amenity a été mise à jour
        updated_response = requests.get(f"{BASE_URL}{amenity_id}")
        updated_data = updated_response.json()
        self.assertEqual(updated_data["name"], "Air Conditioning", "Le nom de l'amenity n'a pas été mis à jour correctement")

    def test_update_amenity_not_found(self):
        """Test mise à jour d'une amenity non existante."""
        update_data = {
            "name": "Air Conditioning"
        }
        response = requests.put(f"{BASE_URL}invalid_id", json=update_data)
        self.assertEqual(response.status_code, 404, "Le serveur devrait renvoyer une erreur 404 pour une amenity non trouvée")

if __name__ == '__main__':
    unittest.main()
