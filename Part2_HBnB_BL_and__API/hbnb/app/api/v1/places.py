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


api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('Amenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('User', {
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
        """Register a new place"""
        # Placeholder for the logic to register a new place
        # pass
        # Logic for registering a new place
        data = api.payload
        if not data:
            api.abort(400, 'Invalid input data')

        title = data['title']
        price = data['price']
        latitude = data['latitude']
        longitude = data['longitude']
        owner_id = data['owner_id']
        amenities = data['amenities']

        # Create a new Place instance
        new_place = facade.create_place(
            title=title,
            description=data.get('description', ''),
            price=price,
            latitude=latitude,
            longitude=longitude,
            owner_id=owner_id,
            amenities=amenities
        )

        # Return the new place details in a dictionary format
        return new_place.to_dict(), 201

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        # Placeholder for logic to return a list of all places
        # pass


@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        # Placeholder for the logic to retrieve a place by ID, including associated owner and amenities
        # pass
        # Logic to retrieve a place by ID, including owner and amenities
        place = facade.get_place_by_id(place_id)
        if place is None:
            api.abort(404, 'Place not found')

        return place.to_dict(), 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        # Placeholder for the logic to update a place by ID
        # pass
        # Logic to update a place by ID
        place = facade.get_place_by_id(place_id)
        if place is None:
            api.abort(404, 'Place not found')

        data = api.payload
        if not data:
            api.abort(400, 'Invalid input data')

        # Update the place's attributes
        if 'title' in data:
            place.title = data['title']
        if 'description' in data:
            place.description = data['description']
        if 'price' in data:
            place.price = data['price']
        if 'latitude' in data:
            place.latitude = data['latitude']
        if 'longitude' in data:
            place.longitude = data['longitude']
        if 'owner_id' in data:
            place.owner_id = data['owner_id']
        if 'amenities' in data:
            place.amenities = data['amenities']

        # Save the updated place information
        updated_place = facade.update_place(place)
        return updated_place.to_dict(), 200

# # Adding the review model
# review_model = api.model('Review', {
#     'id': fields.String(description='Review ID'),
#     'text': fields.String(description='Text of the review'),
#     'rating': fields.Integer(description='Rating of the place (1-5)'),
#     'user_id': fields.String(description='ID of the user')
# })

# place_model = api.model('Place', {
#     'title': fields.String(required=True, description='Title of the place'),
#     'description': fields.String(description='Description of the place'),
#     'price': fields.Float(required=True, description='Price per night'),
#     'latitude': fields.Float(required=True, description='Latitude of the place'),
#     'longitude': fields.Float(required=True, description='Longitude of the place'),
#     'owner_id': fields.String(required=True, description='ID of the owner'),
#     'owner': fields.Nested(user_model, description='Owner of the place'),
#     'amenities': fields.List(fields.Nested(amenity_model), description='List of amenities'),
#     'reviews': fields.List(fields.Nested(review_model), description='List of reviews')
# })
