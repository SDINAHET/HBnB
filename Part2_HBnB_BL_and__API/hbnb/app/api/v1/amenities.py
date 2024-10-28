#!/usr/bin/python3
"""
app/api/v1/amenities.py
This module defines the API endpoints for managing amenities in the HBnB application.
It uses Flask-RESTx for creating and managing API routes and provides functionalities
such as registering, retrieving, and updating amenities.

Routes:
    - POST /api/v1/amenities/: Register a new amenity.
    - GET /api/v1/amenities/: Retrieve a list of all amenities.
    - GET /api/v1/amenities/<amenity_id>: Get details of a specific amenity by its ID.
    - PUT /api/v1/amenities/<amenity_id>: Update an amenity's information.

Models:
    - Amenity: Defines the schema for amenity data used for input validation and documentation.

Error Handling:
    - Returns **201** on successful creation (POST).
    - Returns **200** on successful retrieval and updates (GET, PUT).
    - Returns **400** for invalid input data (POST, PUT).
    - Returns **404** if the requested amenity is not found (GET, PUT).
"""
from flask_restx import Namespace, Resource, fields
from typing import List
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):
    """
    Resource for managing a collection of amenities.

    - POST: Registers a new amenity with specified data.
    - GET: Retrieves a list of all available amenities.
    """

    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """
        Register a new amenity.

        Expects JSON data that contains the "name" field as required by the `amenity_model`.

        Returns:
            - 201 status code with the new amenity data if successful.
            - 400 status code if input data is invalid.
        """
        data = api.payload
        # Validate if 'name' is present in the input data
        if not data or 'name' not in data or data['name'].strip() == "":
            # Abort with a 400 error if validation fails
            api.abort(400, 'Invalid input data: name is required.')
        new_amenity = facade.create_amenity(data)
        return new_amenity.to_dict(), 201


    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """
        Retrieve a list of all amenities.

        Returns:
            - 200 status code with a list of amenities (each with 'id' and 'name').
        """
        # Get all amenities using the facade
        amenities = facade.get_all_amenities()

        # Return only 'id' and 'name' in the response
        response_data = [
            {
                "id": amenity.id,  # Assuming your amenity object has an 'id' attribute
                "name": amenity.name
            }
            for amenity in amenities
        ]
        # Return the list of filtered amenities
        return response_data, 200

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    """
    Resource for managing individual amenities based on `amenity_id`.

    - GET: Retrieves amenity details by ID.
    - PUT: Updates the information of an amenity by ID.
    """

    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """
        Get amenity details by ID.

        Args:
            amenity_id (str): ID of the amenity to retrieve.

        Returns:
            - 200 status code with amenity data if found.
            - 404 status code if the amenity is not found.

        Example:
            GET /api/v1/amenities/12345
        """
        # Retrieve the amenity by ID using the facade
        amenity = facade.get_amenity(amenity_id)

        # If the amenity does not exist, return a 404 error
        if amenity is None:
            api.abort(404, 'Amenity not found')
        # Return only 'id' and 'name' in the response
        response_data = {
            'id': amenity.id,
            'name': amenity.name
        }
        return response_data, 200

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """
        Update an amenity's information by ID.

        Expects JSON data that contains the "name" field as required by the `amenity_model`.

        Args:
            amenity_id (str): ID of the amenity to update.

        Returns:
            - 200 status code with success message if update is successful.
            - 400 status code if input data is invalid.
            - 404 status code if the amenity is not found.
        """
        # Retrieve the amenity by ID to update it
        amenity = facade.get_amenity(amenity_id)

        # If the amenity is not found, return a 404 error
        if amenity is None:
            api.abort(404, 'Amenity not found')
        # Get the input data sent in the request
        data = api.payload
        # Validate that input data is provided
        if not data or 'name' not in data or data['name'].strip() == "":
            api.abort(400, 'Invalid input data: non-empty name is required.')
        facade.update_amenity(amenity_id, data)
        return {'message': 'Amenity updated successfully'}, 200
