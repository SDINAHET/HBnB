# Amenity endpoints code
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade

# Define a namespace for the amenities-related routes
api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):
    """
    Resource for handling requests to create or list amenities.
    """

    @api.doc(description='Register a new amenity')
    @jwt_required()
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """
        Register a new amenity.
        ------------------------

        Parameters:
        -----------
        - `self`: Reference to the instance of the resource class.

        Expects:
        --------
        - JSON payload matching the `amenity_model`, with fields such as:
            - `name` (str): The name of the amenity.

        Returns:
        --------
        - (dict): JSON response with the details of the created amenity, including:
            - `id` (str): Unique identifier of the created amenity.
            - `name` (str): Name of the created amenity.
        - Status code 201 if successful.
        - Status code 400 if data is invalid.

        Raises:
        -------
        - `ValueError`: If input data is invalid or required fields are missing.
        """
        current_user = get_jwt_identity()
        amenity_data = api.payload

        try:
            new_amenity = facade.create_amenity(amenity_data)
            return new_amenity, 201
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.doc(description='Retrieve a list of all amenities')
    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """
        Retrieve a list of all amenities.
        --------------------------------

        Returns:
        --------
        - (list): JSON response with a list of all amenities, each containing:
            - `id` (str): Unique identifier of the amenity.
            - `name` (str): Name of the amenity.
        - Status code 200 if successful.
        """
        amenities = facade.get_all_amenities()
        return amenities, 200

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    """
    Resource for handling requests to get or update a specific amenity.
    """

    @api.doc(description='Get amenity details by ID')
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """
        Get amenity details by ID.
        --------------------------

        Parameters:
        -----------
        - `self`: Reference to the instance of the resource class.
        - `amenity_id` (str): Unique identifier of the amenity to retrieve.

        Returns:
        --------
        - (dict): JSON response with the details of the amenity, including:
            - `id` (str): Unique identifier of the amenity.
            - `name` (str): Name of the amenity.
        - Status code 200 if successful.
        - Status code 404 if the amenity is not found.
        """
        amenity = facade.get_amenity(amenity_id)
        if amenity:
            return amenity, 200
        return {'error': 'Amenity not found'}, 404

    @api.doc(description='Update an amenity by ID')
    @jwt_required()
    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """
        Update an amenity's information by ID.
        --------------------------------------

        Parameters:
        -----------
        - `self`: Reference to the instance of the resource class.
        - `amenity_id` (str): Unique identifier of the amenity to update.

        Expects:
        --------
        - JSON payload matching the `amenity_model`, with fields such as:
            - `name` (str): The name of the amenity.

        Returns:
        --------
        - (dict): JSON response indicating the status of the operation.
        - Status code 200 if successful.
        - Status code 404 if the amenity is not found.
        - Status code 400 if input data is invalid.

        Raises:
        -------
        - `ValueError`: If input data is invalid or required fields are missing.
        """
        current_user = get_jwt_identity()
        amenity_data = api.payload

        try:
            updated_amenity = facade.update_amenity(amenity_id, amenity_data)
            if updated_amenity:
                return updated_amenity, 200
            return {'error': 'Amenity not found'}, 404
        except ValueError as e:
            return {'error': str(e)}, 400
