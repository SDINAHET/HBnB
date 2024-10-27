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

Error Handling:
    - Returns a 201 status code for successful creation (POST).
    - Returns a 200 status code for successful retrieval and updates (GET, PUT).
    - Returns a 400 status code for invalid input data (POST, PUT).
    - Returns a 404 status code if a requested place is not found (GET, PUT).

"""

from flask_restx import Namespace, Resource, fields
from app.services import facade
from app.api.v1.users import api as users_ns  # Import the users namespace
from app.api.v1.users import user_model  # Import user_model directly


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
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
})


@api.route('/')
class PlaceList(Resource):
    """
    Resource for handling requests to list all places or to create a new place.
    """

    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """
        Register a new place.

        Expects:
            - JSON payload matching the place_model, with fields such as title,
              price, location, owner ID, and a list of amenities.

        Returns:
            - JSON response with the details of the created place.
            - 201 status code if successful, or 400 if data is invalid.
        """
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

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """
        Retrieve a list of all places.

        Returns:
            - A list of places, each with minimal details like ID, title, and location.
            - 200 status code upon success.
        """
        places = facade.get_all_places()
        return [{
            'id': place.id,
            'title': place.title,
            'latitude': place.latitude,
            'longitude': place.longitude
        } for place in places], 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    """
    Resource for handling requests for a specific place by its ID.
    """

    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """
        Get the details of a place by its ID.

        Parameters:
            - place_id: The unique identifier for the place.

        Returns:
            - Detailed information about the place, including its title, description,
              owner details, and associated amenities.
            - 200 status code if the place exists, or 404 if it is not found.
        """
        # Logic to retrieve a place by ID, including owner and amenities
        place = facade.get_place(place_id)
        if place is None:
            api.abort(404, 'Place not found')

        # Prepare owner information, handling case if owner is None
        owner_info = {
            'id': place.owner.id if place.owner else None,
            'first_name': place.owner.first_name if place.owner else None,
            'last_name': place.owner.last_name if place.owner else None,
            'email': place.owner.email if place.owner else None
        }

        # Ensure that amenities are correctly populated
        amenities_info = []
        if place.amenities:  # Vérifiez si la place a des IDs d'amenities
            amenities_info = [{
                'id': amenity.id,
                'name': amenity.name
            } for amenity in place.amenities]

        # place = facade.get_place(place_id)

        return {
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner': owner_info,
            'amenities': amenities_info
        }, 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """
        Update the information of a specific place.

        Parameters:
            - place_id: The unique identifier of the place to update.

        Expects:
            - JSON payload with updated fields matching the place_model.

        Returns:
            - Success message with a 200 status code if updated successfully,
              or 400 for invalid data, or 404 if the place is not found.
        """
        # data = api.payload
        # # Validate input data here
        # required_fields = ['title', 'description', 'price', 'latitude', 'longitude']
        # for field in required_fields:
        #     if field not in data:
        #         api.abort(400, f'Missing required field: {field}')

        # try:
        #     updated_place = facade.update_place(place_id, data)
        #     return {'message': 'Place updated successfully'}, 200
        # except ValueError as err:
        #     api.abort(400, str(err))
        # except KeyError:
        #     api.abort(404, 'Place not found')
        data = api.payload

        # Validate input data here
        required_fields = ['title', 'description', 'price', 'latitude', 'longitude']
        for field in required_fields:
            if field not in data:
                api.abort(400, f'Missing required field: {field}')

        # Additional validation for types and values
        if not isinstance(data['title'], str) or not isinstance(data['description'], str):
            api.abort(400, 'Title and description must be strings.')

        if not isinstance(data['price'], (int, float)) or data['price'] < 0:
            api.abort(400, 'Price must be a positive number.')

        if not isinstance(data['latitude'], (int, float)) or not (-90 <= data['latitude'] <= 90):
            api.abort(400, 'Latitude must be a number between -90 and 90.')

        if not isinstance(data['longitude'], (int, float)) or not (-180 <= data['longitude'] <= 180):
            api.abort(400, 'Longitude must be a number between -180 and 180.')

        try:
            updated_place = facade.update_place(place_id, data)
            if updated_place is None:
                api.abort(404, 'Place not found')

            return {'message': 'Place updated successfully'}, 200
        except ValueError as err:
            api.abort(400, str(err))
