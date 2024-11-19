# Place endpoints code
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade

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

# Adding the review model
review_model = api.model('PlaceReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Text of the review'),
    'rating': fields.Integer(description='Rating of the place (1-5)'),
    'user_id': fields.String(description='ID of the user')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place', max_length=100),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night', min=0),
    'latitude': fields.Float(required=True, description='Latitude of the place', min=-90.0, max=90.0),
    'longitude': fields.Float(required=True, description='Longitude of the place', min=-180.0, max=180.0),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
})

@api.route('/')
class PlaceList(Resource):
    """
    Resource for handling requests to list all places or to create a new place.
    """

    @api.doc(description='Register a new place')
    @jwt_required()
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    @api.response(401, 'Missing Authorization Header')
    def post(self):
        """
        Register a new place.

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
        - (dict): JSON response with the details of the created place.
        - Status code 201 if successful.
        - Status code 400 if data is invalid.

        Raises:
        -------
        - `ValueError`: If input data is invalid or required fields are missing.
        """
        current_user = get_jwt_identity()
        payload = api.payload

        # Logic to create a new place using the provided information
        try:
            new_place = facade.create_place(payload, current_user)
            return new_place, 201
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.doc(description='Retrieve a list of all places')
    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """
        Retrieve a list of all places.

        Returns:
        --------
        - (list): JSON list of all places available, including details like:
            - `id`, `title`, `description`, `price`, `latitude`, `longitude`, `owner_id`
        - Status code 200 if successful.
        """
        places = facade.get_all_places()
        return places, 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    """
    Resource for handling requests related to a specific place.
    """

    @api.doc(description='Get details of a specific place by its ID')
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """
        Retrieve details of a specific place.

        Parameters:
        -----------
        - `place_id` (str): Unique identifier of the place to be retrieved.

        Returns:
        --------
        - (dict): JSON details of the requested place.
        - Status code 200 if successful.
        - Status code 404 if place not found.
        """
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        return place, 200

    @jwt_required()
    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(400, 'Invalid input data')
    @api.response(404, 'Place not found')
    @api.response(403, 'Unauthorized action')
    def put(self, place_id):
        """
        Update details of a specific place.

        Parameters:
        -----------
        - `place_id` (str): Unique identifier of the place to be updated.

        Expects:
        --------
        - JSON payload matching the place_model.

        Returns:
        --------
        - (dict): JSON response with the updated details of the place.
        - Status code 200 if successful.
        - Status code 400 if data is invalid.
        - Status code 404 if place not found.
        - Status code 403 if the user is not authorized to update the place.
        """
        current_user = get_jwt_identity()
        payload = api.payload
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        if place['owner_id'] != current_user:
            return {'error': 'Unauthorized action'}, 403
        try:
            updated_place = facade.update_place(place_id, payload)
            return updated_place, 200
        except ValueError as e:
            return {'error': str(e)}, 400
