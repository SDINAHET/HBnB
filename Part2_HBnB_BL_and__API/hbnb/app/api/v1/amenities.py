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
from app.services.facade import HBnBFacade

api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

facade = HBnBFacade()

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        data = api.payload
        # Validate if 'name' is present in the input data
        if not data or 'name' not in data:
            # Abort with a 400 error if validation fails
            api.abort(400, 'Invalid input data: name is required.')
        new_amenity = facade.create_amenity(data)
        return new_amenity.to_dict(), 201

        # Return only 'id' and 'name' in the response
        # response_data = {
        #     "id": new_amenity.id,  # Assuming your amenity object has an 'id' attribute
        #     "name": new_amenity.name
        # }
        # return response_data, 201

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        # Get all amenities using the facade
        amenities = facade.get_all_amenities()

        # Return the list of amenities as dictionaries with a 200 status code
        # return [amenity.to_dict() for amenity in amenities], 200

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
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        # Retrieve the amenity by ID using the facade
        amenity = facade.get_amenity(amenity_id)

        # If the amenity does not exist, return a 404 error
        if amenity is None:
            api.abort(404, 'Amenity not found')
        # Return the amenity's details in dictionary format with a 200 status code
        # return amenity.to_dict(), 200
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
        """Update an amenity's information"""
        # Retrieve the amenity by ID to update it
        amenity = facade.get_amenity(amenity_id)

        # If the amenity is not found, return a 404 error
        if amenity is None:
            api.abort(404, 'Amenity not found')
        # Get the input data sent in the request
        data = api.payload
        # Validate that input data is provided
        # if not data:
        #    api.abort(400, 'Invalid input data: must provide valid fields to update.')
        # updated_amenity = facade.update_amenity(amenity_id, data)
        # return updated_amenity.to_dict(), 200

        # Return the updated amenity's details as a dictionary
        # return {
        #     "id": updated_amenity.id,
        #     "name": updated_amenity.name
        # }, 200
        if not data or 'name' not in data:
            api.abort(400, 'Invalid input data: name is required.')
        facade.update_amenity(amenity_id, data)
        return {'message': 'Amenity updated successfully'}, 200
