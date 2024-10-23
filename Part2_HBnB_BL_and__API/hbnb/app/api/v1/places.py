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
from app.services.facade import HBnBFacade
from app.api.v1.users import api as users_ns  # Import the users namespace
from app.api.v1.users import user_model  # Import user_model directly


api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
# amenity_model = api.model('Amenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
# user_model = api.model('User', {
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

facade = HBnBFacade()

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        data = api.payload
        try:
            new_place = facade.create_place(data)
            return {
                'id': new_place.id,
                'title': new_place.title,
                'description': new_place.description,
                'price': new_place.price,
                'latitude': new_place.latitude,
                'longitude': new_place.longitude,
                'owner_id': new_place.owner_id
            }, 201
            # return new_place.to_dict(), 201
        except ValueError as err:
            api.abort(400, str(err))

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        places = facade.get_all_places()
        # return [place.to_dict() for place in places], 200
        return [{
            'id': place.id,
            'title': place.title,
            'latitude': place.latitude,
            'longitude': place.longitude
        } for place in places], 200


@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        # Logic to retrieve a place by ID, including owner and amenities
        place = facade.get_place_by_id(place_id)
        if place is None:
            api.abort(404, 'Place not found')
        # return place.to_dict(), 200
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
            } for amenity in place.amenities]
        }, 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        # data = api.payload
        # try:
        #     updated_place = facade.update_place(place_id, data)
        #     return updated_place.to_dict(), 200
        # except ValueError as err:
        #     api.abort(400, str(err))
        # except KeyError:
        #     api.abort(404, 'Place not found')
        data = api.payload
        try:
            updated_place = facade.update_place(place_id, data)
            return {'message': 'Place updated successfully'}, 200
        except ValueError as err:
            api.abort(400, str(err))
        except KeyError:
            api.abort(404, 'Place not found')
