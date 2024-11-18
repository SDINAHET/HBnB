#!/usr/bin/python3
"""
app/api/v1/places.py

This module defines the API endpoints for managing places in the HBnB application.
It provides functionalities to create, retrieve, and update place information, including
handling related entities such as the owner (User) and amenities (Amenity). The DELETE
operation for places is not implemented in this part of the project.

The API is built using Flask-RESTx, and the module integrates with the business logic layer
through the HBnBFacade, adhering to a Facade pattern to manage interactions with entities.

Endpoints:
    - POST /api/v1/places/: Register a new place.
    - GET /api/v1/places/: Return a list of all places.
    - GET /api/v1/places/<place_id>: Retrieve details of a specific place, including its associated owner and amenities.
    - PUT /api/v1/places/<place_id>: Update place information.

Models:
    - Place: Defines the schema for place data used for input validation and documentation.
    - Amenity: Represents an associated amenity of a place.
    - User: Represents the owner of a place.

Related Entities:
    - Amenity: A list of amenities that can be linked to a place.
    - User: The owner of the place.

Usage:
    This module is part of the API layer of the HBnB application and interacts with the
    business logic layer to perform place management operations.

"""
from flask_restx import Namespace, Resource, fields
from app.services import facade
# from app.api.v1.users import api as users_ns  # Import the users namespace
# from app.api.v1.users import user_model  # Import user_model directly
from app.services import facade
from app.models.user import User
from app.models.amenity import Amenity  # Assurez-vous d'importer le modèle Amenity
from typing import List, Optional

# app = Flask(__name__)  # *
api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'owner': fields.Nested(user_model, description='Owner details'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
})


@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.doc('create_place')
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        data = api.payload

        # Vérifiez les données d'entrée
        required_fields = ['title', 'description', 'price', 'latitude', 'longitude', 'owner_id']
        for field in required_fields:
            if field not in data:
                api.abort(400, f'Missing required field: {field}')

        try:
            new_place = facade.create_place(data)
            # new_place = facade.create_place(place_data)
            return {
                'id': new_place.id,
                'title': new_place.title,
                'description': new_place.description,
                'price': new_place.price,
                'latitude': new_place.latitude,
                'longitude': new_place.longitude,
                'owner_id': new_place.owner_id
            }, 201
        except ValueError as err:
            api.abort(400, str(err))

    @api.doc('get_all_place')
    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        places = facade.get_all_places()
        return [{
            'id': place.id,
            'title': place.title,
            'latitude': place.latitude,
            'longitude': place.longitude
        } for place in places], 200


@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.doc('get_place_id')
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        # Logic to retrieve a place by ID, including owner and amenities
        # place = facade.get_place_by_id(place_id)
        '''place = facade.get_place(place_id)
        if place is None:
            api.abort(404, 'Place not found')

        # Fetch amenities; ensure your facade method or the Place model handles this
        amenities = place.amenities  # Assuming amenities are a list of amenity objects

        return {
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner': {
                'id': place.owner.id,
                'first_name': place.owner.first_name,
                'last_name': place.owner.last_name,
                'email': place.owner.email
            },
            'amenities': [{
                'id': amenity.id,
                'name': amenity.name
            } for amenity in amenities]
            # } for amenity in amenities if amenity is not None]
            # } for amenity in place.amenities]
            # } for amenity in place.amenities] # if amenity is not None]
            }, 200'''
        '''# Récupération du lieu par ID
        place = facade.get_place(place_id)  # Assurez-vous que cela récupère également les amenities
        if place is None:
            api.abort(404, 'Place not found')

        # Récupération des détails des amenities
        amenities = []
        for amenity_id in place.amenities:  # Supposons que place.amenities est une liste d'IDs
            amenity = facade.get_amenity_by_id(amenity_id)  # Récupérez les détails de chaque amenity
            if amenity:  # Vérifiez que l'amenity existe
                amenities.append({
                    'id': amenity.id,
                    'name': amenity.name
                })

        # Construction de la réponse
        return {
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner': {
                'id': place.owner.id,
                'first_name': place.owner.first_name,
                'last_name': place.owner.last_name,
                'email': place.owner.email
            },
            'amenities': amenities  # Liste des amenities formatée
        }, 200'''
        """Get place details by ID"""

        '''# Récupération du lieu par ID
        place = facade.get_place(place_id)  # Assurez-vous que cela récupère également les amenities
        if place is None:
            api.abort(404, 'Place not found')

        # Supposons que place.amenities est une liste d'IDs
        amenities = []
        for amenity_id in place.amenities:
            # Remplacez ceci par une récupération des détails de l'amenity
            # à partir d'une liste pré-définie ou d'une autre source
            amenity = next((a for a in amenities_list if a["id"] == amenity_id), None)
            if amenity:  # Vérifiez que l'amenity existe
                amenities.append({
                    'id': amenity["id"],
                    'name': amenity["name"]
                })

        # Construction de la réponse
        return {
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner': {
                'id': place.owner.id,
                'first_name': place.owner.first_name,
                'last_name': place.owner.last_name,
                'email': place.owner.email
            },
            'amenities': amenities  # Liste des amenities formatée
        }, 200'''

        """Retrieve a place by its ID."""
        '''place = facade.get_place(place_id)  # Remplacez par votre méthode de récupération

        if place is None:
            return {"message": "Place not found"}, 404

        return place.to_dict(), 200  # Assurez-vous que `to_dict` renvoie les données dans le format requis
        '''
        """Get place details by ID"""

        '''# Récupération du lieu par ID
        place = facade.get_place(place_id)  # Assurez-vous que cela récupère également les amenities
        if place is None:
            api.abort(404, 'Place not found')

        # # Récupération des détails des amenities
        # amenities = []
        # for amenity_id in place.amenities:  # Supposons que place.amenities est une liste d'IDs
        #     # amenity = facade.get_amenity_by_id(amenity_id)  # Récupérez les détails de chaque amenity
        #     amenity = next((a for a in amenities_list if a["id"] == amenity_id), None)
        #     if amenity:  # Vérifiez que l'amenity existe
        #         amenities.append({
        #             # 'id': amenity.id,
        #             # 'name': amenity.name
        #             'id': amenity["id"],
        #             'name': amenity["name"]
        #         })

        # Construction de la réponse
        return {
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner': {
                'id': place.owner.id,
                'first_name': place.owner.first_name,
                'last_name': place.owner.last_name,
                'email': place.owner.email
            },
            'amenities': place.amenities  # Liste des amenities formatée
        }, 200'''
        """Get place details by ID"""
        place = facade.get_place(place_id)
        if place is None:
            api.abort(404, 'Place not found')

        return {
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner': {
                'id': place.owner.id,
                'first_name': place.owner.first_name,
                'last_name': place.owner.last_name,
                'email': place.owner.email
            },
            'amenities': place.amenities  # Liste des amenities formatée
        }, 200

    @api.expect(place_model)
    @api.doc('update_place')
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        data = api.payload
        try:
            # updated_place = facade.update_place(place, data)
            updated_place = facade.update_place(place_id, data)
                    # Pass only non-null values in data to the update function
            # updated_place = facade.update_place(place_id, {k: v for k, v in data.items() if v is not None})
            if updated_place is None:
                api.abort(404, 'Place not found')

            return {'message': 'Place updated successfully'}, 200
        except ValueError as err:
            api.abort(400, str(err))
        # except KeyError:
        #     api.abort(404, 'Place not found')
