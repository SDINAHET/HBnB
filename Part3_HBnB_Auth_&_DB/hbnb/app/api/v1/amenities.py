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
"""
from flask_restx import Namespace, Resource, fields
from typing import List
from app.services import facade
import logging

api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):
    """
    AmenityList class handles the operations related to amenities.

    Methods:
        post: Register a new amenity.
        get: Retrieve a list of all amenities.
    """
    @api.doc(description='Retrieve a list of all amenities')
    # @api.doc(params={'amenity_data': 'Data of the amenity to register'})
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """
        Retrieve a list of all amenities.
        ----------------------------------

        Parameters:
        -----------
        self: The instance of the Resource class.

        Returns:
        --------
        tuple: A tuple containing:
            - List[dict]: List of amenities (id and name).
                -`name` (str): Name of the amenity.
            - int: HTTP status code (200) for successful retrieval.

        Raises:
        -------
        - `ValueError`: If the input data is invalid or required fields are missing.
        - `KeyError`: If the input data does not contain the required keys defined in the amenity_model.
        """

        data = api.payload
        # Validate if 'name' is present in the input data
        if not data or 'name' not in data or data['name'].strip() == "":
            # Abort with a 400 error if validation fails
            api.abort(400, 'Invalid input data: name is required.')
        new_amenity = facade.create_amenity(data)
        return new_amenity.to_dict(), 201


    @api.doc(description='Get amenity details by ID')
    # @api.doc(params={'amenity_id': 'The ID of the amenity to retrieve'})
    @api.response(200, 'List of amenities retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self):
        """
        Get amenity details by ID.
        --------------------------

        Parameters:
        -----------
        self: The instance of the Resource class.
        `amenity_id` (str): The ID of the amenity to retrieve.

        Returns:
        --------
        tuple: A tuple containing:
            - dict: Amenity details (id and name).
                - `id` (str): ID of the amenity.
                - `name` (str): Name of the amenity.
            - int: HTTP status code (200) for successful retrieval.

        Raises:
        -------
        404: If the amenity is not found.
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
    AmenityResource class handles operations for a specific amenity.

    Methods:
        get: Get details of an amenity by its ID.
        put: Update an amenity's information.
    """

    @api.doc(description='Get amenity details by ID')
    @api.doc(params={'amenity_id': 'The ID of the amenity to retrieve'})
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """
        Get amenity details by ID.
        --------------------------

        Parameters:
        -----------
        self: The instance of the Resource class.
        amenity_id (str): The ID of the amenity to retrieve.

        Returns:
        --------
        tuple: A tuple containing:
            - dict: Amenity details (id and name).
                - `id` (str): ID of the amenity.
                - `name` (str): Name of the amenity.
            - int: HTTP status code (200) for successful retrieval.

        Raises:
        -------
        404: If the amenity is not found.
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

    @api.doc(description='Update an amenity by ID')
    @api.doc(params={'amenity_id': 'The ID of the amenity to update'})
    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """
        Put amenity details by ID.
        --------------------------

        Parameters:
        -----------
        self: The instance of the Resource class.
        amenity_id (str): The ID of the amenity to retrieve.

        Returns:
        --------
        tuple: A tuple containing:
            - dict: Amenity details (id and name).
                - `id` (str): ID of the amenity.
                - `name` (str): Name of the amenity.
            - int: HTTP status code (200) for successful retrieval.

        Raises:
        -------
        404: If the amenity is not found.
        """

        # Retrieve the amenity by ID to update it
        amenity = facade.get_amenity(amenity_id)

        # If the amenity is not found, return a 404 error
        if amenity is None:
            api.abort(404, 'Amenity not found')
        # Get the input data sent in the request
        data = api.payload
        # if not data or 'name' not in data or data['name'].strip() == "":
        # if not data or 'name' not in data:
        #     api.abort(400, 'Invalid input data: non-empty name is required.')
        # try:
        updated_amenity = facade.update_amenity(amenity_id, data) # add SD
            # facade.update_amenity(amenity_id, data)
        return {'message': 'Amenity updated successfully'}, 200
        # except Exception as e:
        #     logging.error(f"Error updating amenity: {e}")
        #     api.abort(500, 'Internal Server Error')
