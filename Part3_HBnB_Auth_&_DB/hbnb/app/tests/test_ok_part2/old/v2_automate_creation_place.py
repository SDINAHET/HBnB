#!/usr/bin/python3

import subprocess
import json

# Fonction pour exécuter une commande curl et capturer la réponse
def run_curl(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout, result.returncode

# Fonction pour créer un utilisateur et capturer l'ID et le code de réponse
def create_user():
    user_command = [
        'curl', '-X', 'POST',
        'http://localhost:5000/api/v1/users/',
        '-H', 'accept: application/json',
        '-H', 'Content-Type: application/json',
        '-d', json.dumps({
            "first_name": "John",
            "last_name": "Doe",
            "email": "user.scripte@example.com",
        })
    ]
    user_response, status_code = run_curl(user_command)
    print(f"Response from creating USER (Status Code {status_code}): {user_response}")
    try:
        user_data = json.loads(user_response) if status_code == 201 else {}
    except json.JSONDecodeError:
        print("Erreur : la réponse de création de l'utilisateur n'est pas au format JSON.")
        return None, status_code
    return user_data.get('id'), status_code

# Fonction pour créer une amenity et capturer l'ID et le code de réponse
def create_amenity():
    amenity_command = [
        'curl', '-X', 'POST',
        'http://localhost:5000/api/v1/amenities/',
        '-H', 'accept: application/json',
        '-H', 'Content-Type: application/json',
        '-d', json.dumps({
            "name": "WI-FI_test"
        })
    ]
    amenity_response, status_code = run_curl(amenity_command)
    print(f"Response from creating AMENITY (Status Code {status_code}): {amenity_response}")
    try:
        amenity_data = json.loads(amenity_response) if status_code == 201 else {}
    except json.JSONDecodeError:
        print("Erreur : la réponse de création de l'amenity n'est pas au format JSON.")
        return None, status_code
    return amenity_data.get('id'), status_code

# Fonction pour créer une place et capturer l'ID et le code de réponse
def create_place(owner_id, amenity_id):
    if not owner_id or not amenity_id:
        print("Erreur : l'ID de l'utilisateur ou de l'amenity est manquant, création de la place impossible.")
        return None, 400  # Code 400 : mauvaise requête due aux dépendances manquantes
    place_command = [
        'curl', '-X', 'POST',
        'http://localhost:5000/api/v1/places/',
        '-H', 'accept: application/json',
        '-H', 'Content-Type: application/json',
        '-d', json.dumps({
            "title": "maison rennes",
            "description": "un cha23let rennais",
            "price": 12,
            "latitude": 52.1,
            "longitude": 14.2,
            "owner_id": owner_id,
            "amenities": [amenity_id]
        })
    ]
    place_response, status_code = run_curl(place_command)
    print(f"Response from creating PLACE (Status Code {status_code}): {place_response}")
    try:
        place_data = json.loads(place_response) if status_code == 201 else {}
    except json.JSONDecodeError:
        print("Erreur : la réponse de création de la place n'est pas au format JSON.")
        return None, status_code
    return place_data.get('id'), status_code

if __name__ == "__main__":
    # Création de l'utilisateur
    user_id, user_status_code = create_user()

    # Création de l'amenity
    amenity_id, amenity_status_code = create_amenity()

    # Création de la place
    place_id, place_status_code = create_place(user_id, amenity_id)

    # Résumé des résultats
    print("\n=== Résumé de la création ===")
    print(f"Utilisateur (user_id) : {user_id if user_id else 'Non créé'} - Code de statut : {user_status_code}")
    print(f"Amenity (amenity_id) : {amenity_id if amenity_id else 'Non créé'} - Code de statut : {amenity_status_code}")
    print(f"Place (place_id) : {place_id if place_id else 'Non créé'} - Code de statut : {place_status_code}")
