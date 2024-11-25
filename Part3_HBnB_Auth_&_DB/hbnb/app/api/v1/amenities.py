#!/usr/bin/python3
"""
This module defines the API endpoints for managing amenities in the HBnB application.
It implements the routes for creating, retrieving, and updating amenities.

Routes:
    POST /api/v1/amenities/ : Add a new amenity (Admin only).
    PUT /api/v1/amenities/<amenity_id> : Modify the details of an amenity (Admin only).
    GET /api/v1/amenities/ : Get the list of all amenities.
    GET /api/v1/amenities/<amenity_id> : Get a specific amenity by ID.
    PUT /api/v1/amenities/<amenity_id> : Update an amenity's information.
"""

from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.exceptions import BadRequest, NotFound, Forbidden
from flask import request


api = Namespace('amenities', description='Amenity operations')

amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

amenity_update_model = api.model('AmenityUpdate', {
    'name': fields.String(description='Updated name of the amenity'),
})

# -------------------------- Create a New Amenity (Admin Only) --------------------------
@api.route('/')
class AmenityCreate(Resource):
    @jwt_required()  # L'authentification est requise
    @api.expect(amenity_model, validate=True)
    @api.doc(description='Admin: Register a new amenity.', security='BearerAuth')
    @api.response(201, 'Amenity successfully created')
    @api.response(403, 'Admin privileges required')
    @api.response(400, 'Invalid input data')
    def post(self):
        """
        Create a new amenity.
        This route allows anyone to create a new amenity.
        """
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            raise Forbidden('Admin privileges required')

        amenity_data = request.json
        if not amenity_data.get('name'):
            raise BadRequest('Amenity name is required.')

        try:
            new_amenity = facade.create_amenity(amenity_data)
            return {
                'message': 'Amenity created successfully',
                'amenity_id': new_amenity.id,
            }, 201
        except Exception as e:
            raise BadRequest(f'An error occurred while creating the amenity: {str(e)}')

# -------------------------- Retrieve Amenity by ID --------------------------

@api.route('/update/<amenity_id>')
class AmenityResource(Resource):
    @api.doc(description='Retrieve a specific amenity by ID.')
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """
        Get details of a specific amenity by its ID.
        """
        amenity = facade.get_amenity(amenity_id)

        if not amenity:
            raise NotFound('Amenity not found')

        return {
            'id': amenity.id,
            'name': amenity.name
        }, 200

# -------------------------- Update Amenity by ID --------------------------

@api.route('/<amenity_id>')
class AmenityUpdate(Resource):
    @jwt_required()  # L'authentification est requise
    @api.expect(amenity_update_model, validate=True)
    @api.doc(description='Admin: Update an amenity by ID.', security='BearerAuth')
    @api.response(200, 'Amenity updated successfully')
    @api.response(403, 'Admin privileges required')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """
        Update an amenity's details by ID.
        This route allows only admins to update an amenity.
        """
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            raise Forbidden('Admin privileges required')

        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            raise NotFound('Amenity not found')

        updated_data = request.json
        if 'name' not in updated_data:
            raise BadRequest('Name field is required.')

        try:
            updated_amenity = facade.update_amenity(amenity_id, updated_data)
            return {
                'message': 'Amenity updated successfully',
                'amenity_id': updated_amenity.id,
                'name': updated_amenity.name,
            }, 200
        except Exception as e:
            raise BadRequest(f'An error occurred while updating the amenity: {str(e)}')

# -------------------------- Admin-Only Routes --------------------------

@api.route('/admin/<amenity_id>')
class AdminAmenityUpdate(Resource):
    @jwt_required()
    @api.expect(amenity_update_model, validate=True)
    @api.doc(description='Admin: Update an amenity by ID.', security='BearerAuth')
    @api.response(200, 'Amenity updated successfully')
    @api.response(403, 'Admin privileges required')
    @api.response(404, 'Amenity not found')
    def put(self, amenity_id):
        """
        Admin-only route to update an amenity by ID.
        Admins can update any amenity details.
        """
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            raise Forbidden('Admin privileges required')

        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            raise NotFound('Amenity not found')

        updated_data = request.json
        if 'name' not in updated_data:
            raise BadRequest('Name field is required.')

        try:
            updated_amenity = facade.update_amenity(amenity_id, updated_data)
            return {
                'message': 'Amenity updated successfully',
                'amenity_id': updated_amenity.id,
                'name': updated_amenity.name,
            }, 200
        except Exception as e:
            raise BadRequest(f'An error occurred while updating the amenity: {str(e)}')


# -------------------------- Admin Routes to List All Amenities --------------------------

@api.route('/admin/')
class AdminAmenityList(Resource):
    @jwt_required()
    @api.doc(description='Admin: Get the list of all amenities.', security='BearerAuth')
    @api.response(200, 'List of amenities retrieved successfully')
    @api.response(403, 'Admin privileges required')
    def get(self):
        """
        Admin-only route to get a list of all amenities.
        """
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            raise Forbidden('Admin privileges required')

        amenities = facade.get_all_amenities()
        if not amenities:
            raise NotFound('No amenities found.')

        return [
            {
                'id': amenity.id,
                'name': amenity.name,
            }
            for amenity in amenities
        ], 200
