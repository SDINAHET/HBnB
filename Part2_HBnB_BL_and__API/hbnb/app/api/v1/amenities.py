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
        # Placeholder for the logic to register a new amenity
        # pass
        data = api.payload
        # Validate if 'name' is present in the input data
        if not data or 'name' not in data:
            # Abort with a 400 error if validation fails
            api.abort(400, 'Invalid input data: name is required.')

        # Extract 'name' and 'description' (optional) from the input data
        name = data['name']
        description = data.get('description', '')

        # Create a new Amenity instance with the provided data
        new_amenity = Amenity(name=name, description=description)

        # Save the new amenity using the facade's business logic
        saved_amenity = facade.create_amenity(new_amenity)

        # Return the saved amenity in dictionary format and a 201 status code
        return saved_amenity.to_dict(), 201

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        # Placeholder for logic to return a list of all amenities
        # pass
        # Get all amenities using the facade
        amenities = facade.get_all_amenities()

        # Return the list of amenities as dictionaries with a 200 status code
        return [amenity.to_dict() for amenity in amenities], 200

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        # Placeholder for the logic to retrieve an amenity by ID
        # pass
        # Retrieve the amenity by ID using the facade
        amenity = facade.get_amenity_by(amenity_id)

        # If the amenity does not exist, return a 404 error
        if amenity is None:
            api.abort(404, 'Amenity not found')

        # Return the amenity's details in dictionary format with a 200 status code
        return amenity.to_dict(), 200

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        # Placeholder for the logic to update an amenity by ID
        # pass
        # Retrieve the amenity by ID to update it
        amenity = facade.get_amenity_by(amenity_id)

        # If the amenity is not found, return a 404 error
        if amenity is None:
            api.abort(404, 'Amenity not found')

        # Get the input data sent in the request
        data = api.payload
        # Validate that input data is provided
        if not data:
            api.abort(400, 'Invalid input data: must provide valid fields to update.')

        # Update the amenity fields if they are provided in the input data
        if 'name' in data:
            amenity.name = data['name']
        if 'description' in data:
            amenity.description = data['description']

        # Save the updated amenity using the facade
        updated_amenity = facade.update_amenity(amenity)

        # Return the updated amenity details with a 200 status code
        return updated_amenity.to_dict(), 200
