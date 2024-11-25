#!/usr/bin/python3

import subprocess
import json

# print("""
#                     '-.,;;:;,
#                      _;\;|\;:;,
#                     ) __ ' \;::,
#                 .--'  e   ':;;;:,           ;,
#                (^           ;;::;          ;;;,
#        _        --_.--.___,',:;::;     ,,,;:;;;,
#       < \        `;     |  ;:;;:;        ':;:;;;,,
#     <`-; \__     ,;    /    ';:;;:,       ';;;'
#     <`_   __',   ; ,  /    ::;;;:         //
#        `)|  \ \   ` .'      ';;:;,       //
#         `    \ `\  /        ;;:;;.      //__
#               \  `/`         ;:;  ~._,=~`   `~=,
#                \_|      (        ^     ^  ^ _^  \
#                  \    _,`      / ^ ^  ^   .' `.^ ;
#         <`-.  #C24 '-;`       /`  ^   ^  /\    ) ^/
#         <'- \__..-'` ___,,,-'._ ^  ^ _.'\^`'-' ^/
#          `)_   ..-''`          `~~~~`    `~===~`
#          <_.-`-._\
# """)

# Fonction pour exécuter une commande curl et retourner la sortie
def run_curl(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# Étape 1 : Créer un utilisateur
user_command = [
    'curl', '-X', 'POST',
    'http://localhost:5000/api/v1/users/',
    '-H', 'accept: application/json',
    '-H', 'Content-Type: application/json',
    '-d', json.dumps({
        "email": "user@example.com",
        "first_name": "John",
        "last_name": "Doe"
    })
]

user_response = run_curl(user_command)
print("Response from creating USER:", user_response)
user_data = json.loads(user_response)

# Étape 2 : Créer la première amenity
amenity_command_1 = [
    'curl', '-X', 'POST',
    'http://localhost:5000/api/v1/amenities/',
    '-H', 'accept: application/json',
    '-H', 'Content-Type: application/json',
    '-d', json.dumps({
        "name": "Wi-Fi_test"  # Première amenity
    })
]

amenity_response_1 = run_curl(amenity_command_1)
print("Response from creating AMENITY 1:", amenity_response_1)
amenity_data_1 = json.loads(amenity_response_1)

# Étape 2 : Créer la deuxième amenity
amenity_command_2 = [
    'curl', '-X', 'POST',
    'http://localhost:5000/api/v1/amenities/',
    '-H', 'accept: application/json',
    '-H', 'Content-Type: application/json',
    '-d', json.dumps({
        "name": "Air Conditioning_test"  # Deuxième amenity
    })
]

amenity_response_2 = run_curl(amenity_command_2)
print("Response from creating AMENITY 2:", amenity_response_2)
amenity_data_2 = json.loads(amenity_response_2)

# Étape 3 : Créer une place en utilisant l'ID de l'amenity et de l'utilisateur créés
place_command = [
    'curl', '-X', 'POST',
    'http://localhost:5000/api/v1/places/',
    '-H', 'accept: application/json',
    '-H', 'Content-Type: application/json',
    '-d', json.dumps({
        "title": "Maison Rennes",
        "description": "Un chalet Rennais au soleil",
        "price": 120,
        "latitude": 37.7749,
        "longitude": -122.4194,
        "owner_id": user_data['id'],  # Utilisation de l'ID de l'utilisateur
        "amenities": [amenity_data_1['id'], amenity_data_2['id']]  # Utilisation des IDs des amenities
    })
]

place_response = run_curl(place_command)
print("Response from creating a place:", place_response)
print("Raw response from creating a place:", place_response)

# place_data = json.loads(place_response) if place_response else {}

try:
    place_data = json.loads(place_response)
except json.JSONDecodeError as e:
    print("JSON decoding error:", e)
    place_data = {}

# # Étape 4 : Mettre à jour la place avec les données récupérées
# place_id = place_data.get('id')  # Assurez-vous que place_data a été défini précédemment
# owner_id = user_data.get('id')  # ID de l'utilisateur créé
# amenity_id_1 = amenity_data_1.get('id')  # ID de la première amenity
# amenity_id_2 = amenity_data_2.get('id')  # ID de la deuxième amenity

# # JSON à envoyer pour la mise à jour
# update_data = {
#     "title": "maison laval2",
#     "description": "holert....",
#     "price": 23,
#     "latitude": 56.1,
#     "longitude": 23.1,
#     "owner_id": owner_id,  # ID de l'utilisateur
#     "amenities": [amenity_id_1, amenity_id_2]  # Utilisation des IDs des amenities
# }

# # Commande pour mettre à jour la place
# update_place_command = [
#     'curl', '-X', 'PUT',
#     f'http://localhost:5000/api/v1/places/{place_id}',
#     '-H', 'accept: application/json',
#     '-H', 'Content-Type: application/json',
#     '-d', json.dumps(update_data)  # Utilisation du JSON préparé
# ]

# update_place_response = run_curl(update_place_command)
# print("Response from updating the place:", update_place_response)

# # Vérifier la réponse de la mise à jour
# updated_place_data = json.loads(update_place_response) if update_place_response else {}

# Résumé final des IDs créés
print("\n=== Résumé de la création ===")
print(f"ID Utilisateur : {user_data.get('id', 'Non créé')}")
print(f"ID Amenity 1 : {amenity_data_1.get('id', 'Non créé')}")
print(f"ID Amenity 2 : {amenity_data_2.get('id', 'Non créé')}")
print(f"ID Place : {place_data.get('id', 'Non créé')}")
print("""
██╗  ██╗██████╗ ███╗   ██╗██████╗
██║  ██║██╔══██╗████╗  ██║██╔══██╗
███████║███████║██╔██╗ ██║███████║
██╔══██║██║  ██║██║╚██╗██║██║  ██║
██║  ██║██████╔╝██║ ╚████║██████╔╝
╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═══╝╚═════╝
 | HBnB Logo  # C24
""")
