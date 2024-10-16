#!/usr/bin/python3
"""
This module defines the API endpoints for user management in the HBnB application.
It implements the routes for creating, retrieving, and updating users.

Routes:
    POST /api/v1/users/ : Create a new user.
    GET /api/v1/users/ : Get the list of all users.
    GET /api/v1/users/<user_id> : Get a specific user by ID.
    PUT /api/v1/users/<user_id> : Update a user's information.
"""

from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade
from app.models.user import User

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user')
})

facade = HBnBFacade()


@api.route('/')
class UserList(Resource):
    """
    Resource class for handling user creation and retrieval of all users.
    
    Methods:
        post: Registers a new user.
        get: Retrieves a list of all users.
    """
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """
        Register a new user.
        
        This method handles the registration of a new user, checks for email uniqueness, 
        and returns the user details if successfully created.
        
        Returns:
            dict: A dictionary containing the new user's details.
            int: The HTTP status code (201 on success, 400 on failure).
        """

        user_data = api.payload

        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        new_user = facade.create_user(user_data)
        return {
            'id': new_user.id,
            'first_name': new_user.first_name,
            'last_name': new_user.last_name,
            'email': new_user.email
            }, 201

    @api.response(200, 'List of users retrieved successfully')
    @api.response(404, 'No users found')
    def get(self):
        """
        Retrieve the list of all users.
        
        This method retrieves all registered users. If no users are found, a 404 error is returned.
        
        Returns:
            list: A list of dictionaries containing user details.
            int: The HTTP status code (200 on success, 404 on failure).
        """

        users = facade.get_all_users()
        if not users:
            return {'error': 'No users found'}, 404
        return [{
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
            } for user in users], 200


@api.route('/<user_id>')
class UserResource(Resource):
    """
    Resource class for handling individual user operations: retrieval and update.
    
    Methods:
        get: Retrieves a specific user by their ID.
        put: Updates a user's information.
    """

    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """
        Retrieve a user's details by ID.
        
        This method retrieves the details of a user with the given user_id. If the user is not found, a 404 error is returned.
        
        Args:
            user_id (str): The ID of the user to retrieve.
        
        Returns:
            dict: A dictionary containing the user's details.
            int: The HTTP status code (200 on success, 404 on failure).
        """

        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
            }, 200

    @api.expect(user_model, validate=True)
    @api.reponse(200, 'User successfully updated')
    @api.response(404, 'User not found')
    def put(self, user_id):
        """
        Update a user's details by ID.
        
        This method updates the details of a user with the given user_id. If the user is not found, a 404 error is returned.
        
        Args:
            user_id (str): The ID of the user to update.
        
        Returns:
            dict: A dictionary containing the updated user's details.
            int: The HTTP status code (200 on success, 404 on failure).
        """

        user_data = api.payload
        updated_user = facade.update_user(user_id, user_data)
        if not updated_user:
            return {'error': 'User not found'}, 404
        return {
            'id': updated_user.id,
            'first_name': updated_user.first_name,
            'last_name': updated_user.last_name,
            'email': updated_user.email
        }, 200
