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
from flask_jwt_extended import jwt_required, get_jwt_identity # add SD
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

    @api.doc(description='Register a new place')
    # @api.doc(params={'place_data': 'Data of the place to register'})
    @jwt_required() # add SD
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    @api.response(401, 'Missing Authorization Header')
    def post(self):
        """
        Register a new place.
        ----------------------

        Parameters:
        -----------
        - `self`: Reference to the instance of the resource class.

        Expects:
        --------
        - JSON payload matching the place_model, with fields such as:
            - `title` (str): Title of the place.
            - `description` (str): Description of the place.
            - `price` (float): Price per night.
            - `latitude` (float): Latitude of the place.
            - `longitude` (float): Longitude of the place.
            - `owner_id` (str): ID of the owner.
            - `amenities` (list): List of amenities ID's.

        Returns:
        --------
        - (dict): JSON response with the details of the created place, including:
            - `id` (str): Unique identifier of the created place.
            - `title` (str): Title of the created place.
            - `description` (str): Description of the created place.
            - `price` (float): Price per night of the created place.
            - `latitude` (float): Latitude of the created place.
            - `longitude` (float): Longitude of the created place.
            - `owner_id` (str): ID of the owner of the created place.
        - Status code 201 if successful.
        - Status code 400 if data is invalid.

        Raises:
        -------
        - `ValueError`: If input data is invalid or required fields are missing.
        """
        current_user = get_jwt_identity() # add SD
        data = api.payload
        # data['owner_id'] = current_user  # Ajoutez cette ligne pour définir owner_id

       # Vérifiez les données d'entrée
        required_fields = ['title', 'description', 'price', 'latitude', 'longitude', 'owner_id']
        for field in required_fields:
            if field not in data:
                api.abort(400, f'Missing required field: {field}')

        try:
            # new_place = facade.create_place(data) # old
            # new_place = facade.create_place(place_data) #ne pas utiliser
            # new_place = facade.create_place(owner_id=current_user, **data) # add SD
            new_place = facade.create_place(data)
            return {
                'id': new_place.id,
                'title': new_place.title,
                'description': new_place.description,
                'price': new_place.price,
                'latitude': new_place.latitude,
                'longitude': new_place.longitude,
                'owner_id': new_place.owner_id,
                'amenities': [amenity.id for amenity in new_place.amenities]
            }, 201
        except ValueError as err:
            api.abort(400, str(err))

    @api.doc(description='Retrieve the list of all places')
    # @api.doc(params={'place_id': 'The ID of the place to retrieve'})
    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """
        Retrieve a list of all places.
        -------------------------------

        Parameters:
        ----------
        - `self`: Reference to the instance of the resource class.

        Expects:
        --------
        - No additional parameters.

        Returns:
        --------
        - (list): A list of places, each represented as a dictionary containing:
            - `id` (str): Unique identifier of the place.
            - `title` (str): Title of the place.
            - `latitude` (float): Latitude of the place.
            - `longitude` (float): Longitude of the place.
        - Status code 200 upon success.
        """

        places = facade.get_all_places()
        if not places: # add SD
            return {'error': 'No places found'}, 404 # add SD
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

    @api.doc(description='Retrieve details of a specific place by ID')
    @api.doc(params={'place_id': 'The ID of the place to retrieve'})
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """
        Get the details of a place by its ID.
        --------------------------------------

        Parameters:
        -----------
        - `self`: Reference to the instance of the resource class.
        - `place_id` (str): The unique identifier for the place.

        Expects:
        --------
        - No additional parameters.

        Returns:
        --------
        - (dict): Detailed information about the place, including:
            - `id` (str): Unique identifier of the place.
            - `title` (str): Title of the place.
            - `description` (str): Description of the place.
            - `latitude` (float): Latitude of the place.
            - `longitude` (float): Longitude of the place.
            - `owner` (dict): Information about the owner, including:
        - Status code 200 if the place exists.
        - Status code 404 if the place is not found.

        Raises:
        - `ValueError`: If an unexpected error occurs while retrieving the place.
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

    @api.doc(description='Update a specific place by ID')
    @api.doc(params={'place_id': 'The ID of the place to update'})
    @jwt_required() # add SD
    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(401, 'Missing Authorization Header')
    @api.response(403, 'Unauthorized action')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """
        Update the information of a specific place.
        -------------------------------------------

        Parameters:
        -----------
        - `self`: Reference to the instance of the resource class.
        - `place_id` (str): The unique identifier of the place to update.

        Expects:
        --------
        - JSON payload with updated fields matching the place_model, including:
            - `title` (str): Updated title of the place.
            - `description` (str): Updated description of the place.
            - `price` (float): Updated price per night.
            - `latitude` (float): Updated latitude of the place.
            - `longitude` (float): Updated longitude of the place.

        Returns:
        --------
        - (dict): Success message indicating the place was updated successfully.
        - Status code 200 if updated successfully.
        - Status code 400 if data is invalid.
        - Status code 404 if the place is not found.

        Raises:
        -------
        - `ValueError`: If input data is invalid or required fields are missing.
        - `KeyError`: If the specified place ID does not correspond to an existing place.
        """
        current_user = get_jwt_identity()
        data = api.payload

        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404

        if place.owner_id != current_user:
            return {'error': 'Unauthorized action'}, 403

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
           # updated_place = facade.update_place(place_id, data) # old
            updated_place = facade.update_place(place_id, **data) # add SD
            if updated_place is None:
                api.abort(404, 'Place not found')

            return {'message': 'Place updated successfully'}, 200
        except ValueError as err:
            api.abort(400, str(err))
