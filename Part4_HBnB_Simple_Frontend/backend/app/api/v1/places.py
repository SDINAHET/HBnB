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
from flask import request, jsonify

api = Namespace('places', description='Place operations')

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

review_model = api.model('PlaceReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Text of the review'),
    'rating': fields.Integer(description='Rating of the place (1-5)'),
    'user_id': fields.String(description='ID of the user')
})

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

    @api.doc(description='Register a new place') #, security='BearerAuth')
    @jwt_required()
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    @api.response(401, 'Missing Authorization Header')
    def post(self):
        """
        Register a new place.

        Expects a JSON payload matching the place_model, with fields such as:
        - `title` (str): Title of the place.
        - `description` (str): Description of the place.
        - `price` (float): Price per night.
        - `latitude` (float): Latitude of the place.
        - `longitude` (float): Longitude of the place.
        - `owner_id` (str): ID of the owner.
        - `amenities` (list): List of amenities IDs.
        """
        current_user = get_jwt_identity()
        data = api.payload
        data['owner_id'] = current_user['id'] # add SD

        required_fields = ['title', 'description', 'price', 'latitude', 'longitude', 'owner_id']
        for field in required_fields:
            if field not in data:
                api.abort(400, f'Missing required field: {field}')

        try:
            new_place = facade.create_place(
                title=data['title'],
                description=data['description'],
                price=data['price'],
                latitude=data['latitude'],
                longitude=data['longitude'],
                owner_id=data['owner_id'],
                amenities=data['amenities']
            )
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
    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """
        Retrieve a list of all places.
        """
        places = facade.get_all_places()
        if not places:
            return {'error': 'No places found'}, 404
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
        """

        place = facade.get_place(place_id)
        if place is None:
            api.abort(404, 'Place not found')

        owner_info = {
            'id': place.owner.id if place.owner else None,
            'first_name': place.owner.first_name if place.owner else None,
            'last_name': place.owner.last_name if place.owner else None,
            'email': place.owner.email if place.owner else None
        }

        return {
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'price': place.price,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner': owner_info,
            'amenities': [{
                'id': amenity.id,
                'name': amenity.name
            } for amenity in place.amenities],
            'reviews': [{
                'id': review.id,
                'text': review.text,
                'rating': review.rating,
                'user_id': review.user.id
            } for review in place.reviews]
        }, 200

    @api.doc(description='Update a specific place by ID', security='BearerAuth')
    @api.doc(params={'place_id': 'The ID of the place to update'})
    @jwt_required()
    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(401, 'Missing Authorization Header')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """
        Update the information of a specific place.
        """
        current_user = get_jwt_identity()

        is_admin = current_user.get('is_admin')

        place = facade.get_place(place_id)
        if not place:
            api.abort(404, 'Unauthorized to update this place')

        if str(place.owner_id) != str(current_user['id']) and not is_admin:
            api.abort(403, "Unauthorized action")

        data = api.payload
        try:
            updated_place = facade.update_place(place_id, data)
            return {
                'id': updated_place.id,
                'title': updated_place.title,
                'description': updated_place.description,
                'price': updated_place.price,
                'latitude': updated_place.latitude,
                'longitude': updated_place.longitude,
                'owner_id': updated_place.owner_id,
                'amenities': [amenity.id for amenity in updated_place.amenities]
            }, 200
        except ValueError as err:
            api.abort(400, str(err))


    @api.doc('delete_place', security='BearerAuth')
    @api.response(204, 'Place deleted')
    @api.response(401, 'Missing Authorization Header')
    @api.response(403, 'Unauthorized action')
    @api.response(404, 'Place not found')
    @jwt_required()
    def delete(self, place_id):
        """Delete a place - Owner only"""
        try:
            current_user = get_jwt_identity()

            is_admin = current_user.get('is_admin')

            place = facade.get_place(place_id)
            if not place:
                api.abort(404, "Place not found")

            if str(place.owner_id) != str(current_user['id']) and not is_admin:
                api.abort(403, "Unauthorized action")

            facade.delete_place(place_id)
            return '', 204

        except Exception:
            api.abort(500, 'Internal Server Error')
