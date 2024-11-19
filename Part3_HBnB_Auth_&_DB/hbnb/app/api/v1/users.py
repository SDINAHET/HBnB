# User endpoints code
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """
        Register a new user.
        ----------------------

        Parameters:
        -----------
        - `self`: Reference to the instance of the resource class.

        Expects:
        --------
        - JSON payload matching the user_model, with fields such as:
            - `first_name` (str): First name of the user.
            - `last_name` (str): Last name of the user.
            - `email` (str): Email of the user.

        Returns:
        --------
        - (dict): JSON response with the details of the created user.
            - `id` (str): Unique identifier of the created user.
            - `first_name` (str): First name of the created user.
            - `last_name` (str): Last name of the created user.
            - `email` (str): Email of the created user.
        - Status code 201 if successful.
        - Status code 400 if data is invalid.

        Raises:
        -------
        - `ValueError`: If input data is invalid or required fields are missing.
        """
        user_data = api.payload
        try:
            new_user = facade.create_user(user_data)
            return new_user, 201
        except ValueError as e:
            return {'error': str(e)}, 400

@api.route('/<user_id>')
class UserResource(Resource):
    @jwt_required()
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """
        Get user details by ID.
        ------------------------

        Parameters:
        -----------
        - `self`: Reference to the instance of the resource class.
        - `user_id` (str): The unique identifier of the user to retrieve.

        Returns:
        --------
        - (dict): JSON response with the details of the user.
        - Status code 200 if successful.
        - Status code 404 if the user is not found.

        Raises:
        -------
        - `ValueError`: If the user with the given ID does not exist.
        """
        try:
            current_user = get_jwt_identity()
            if current_user != user_id:
                return {'error': 'Unauthorized action'}, 403
            user = facade.get_user(user_id)
            return user, 200
        except ValueError as e:
            return {'error': str(e)}, 404

    @jwt_required()
    @api.expect(user_model)
    @api.response(200, 'User updated successfully')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Unauthorized action')
    def put(self, user_id):
        """
        Update user information.
        -------------------------

        Parameters:
        -----------
        - `self`: Reference to the instance of the resource class.
        - `user_id` (str): The unique identifier of the user to update.

        Expects:
        --------
        - JSON payload matching the user_model with updated values.

        Returns:
        --------
        - Status code 200 if update is successful.
        - Status code 400 if data is invalid.
        - Status code 403 if user is unauthorized.

        Raises:
        -------
        - `ValueError`: If input data is invalid.
        - `PermissionError`: If the user attempts to modify data that does not belong to them.
        """
        user_data = api.payload
        current_user = get_jwt_identity()
        if current_user != user_id:
            return {'error': 'Unauthorized action'}, 403
        try:
            updated_user = facade.update_user(user_id, user_data)
            return updated_user, 200
        except ValueError as e:
            return {'error': str(e)}, 400
