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

import logging
from marshmallow import fields, ValidationError
from flask_restx import Namespace, Resource, fields
from app.services import facade
import re  # Add this for email validation

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user'),
    'is_admin': fields.Boolean(required=False, default=False, description='Is the user an admin')  # Ajout du champ isAdmin
    })


logging.basicConfig(level=logging.INFO)  # Or DEBUG, depending on your needs

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
            tuple: A tuple containing:
                - dict: A dictionary with the new user's details.
                - int: The HTTP status code (201 on success, 400 on failure).

        Raises:
            ValidationError: If input data fails validation checks.
            ValueError: If the email is already registered.
        """

        user_data = api.payload

        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
        # if existing_user and existing_user.id != user_id:  # fix Erwan
            return {'error': 'Email already registered'}, 400

        try:
            new_user = facade.create_user(user_data)
            new_user.hash_password(user_data['password'])
            return {
                'id': new_user.id,
                'first_name': new_user.first_name,
                'last_name': new_user.last_name,
                'email': new_user.email,
            }, 201
        except ValidationError as ve:
            return {'error': ve.messages}, 400
        except Exception as e:
            return {'error': str(e)}, 400

    @api.response(200, 'List of users retrieved successfully')
    @api.response(404, 'No users found')
    def get(self):
        """
        Retrieve the list of all users.

        This method retrieves all registered users. If no users are found, a 404 error is returned.

        Returns:
            tuple: A tuple containing:
                - list: A list of dictionaries with user details.
                - int: The HTTP status code (200 on success, 404 on failure).
        """
        users = facade.get_all_users()
        if not users:
            return {'error': 'No users found'}, 404
        return [{
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
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
            tuple: A tuple containing:
                - dict: A dictionary with the user's details.
                - int: The HTTP status code (200 on success, 404 on failure).
        """

        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            }, 200

    @api.expect(user_model, validate=True)
    @api.response(200, 'User successfully updated')
    @api.response(404, 'User not found')
    @api.response(400, 'Invalid input data')
    def put(self, user_id):
        """
        Update a user's details by ID.

        This method updates the details of a user with the given user_id. If the user is not found, a 404 error is returned.

        Args:
            user_id (str): The ID of the user to update.

        Returns:
            tuple: A tuple containing:
                - dict: A dictionary with the updated user's details.
                - int: The HTTP status code (200 on success, 404 on failure).

        Raises:
            ValueError: If required fields are missing or the email format is invalid.
            Exception: For any other unexpected errors.
        """

        # Récupérer les données envoyées dans la requête
        user_data = api.payload

        # Essayer de mettre à jour l'utilisateur
        try:
            if not user_data.get('first_name'):
                raise ValueError("First name is required.")
            if not user_data.get('last_name'):
                raise ValueError("Last name is required.")

            # Optional: Validate email format
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if 'email' in user_data and not re.match(email_pattern, user_data['email']):
                raise ValueError("Invalid email format.")

            # Tentez de mettre à jour l'utilisateur dans le système
            updated_user = facade.update_user(user_id, user_data)

            # Vérifier si l'utilisateur a été trouvé
            if not updated_user:
                return {'error': 'User not found'}, 404

            # Si l'utilisateur a été mis à jour avec succès, renvoyez les détails
            return {
                'id': updated_user.id,
                'first_name': updated_user.first_name,
                'last_name': updated_user.last_name,
                'email': updated_user.email,
            }, 200

        except Exception as e:
            logging.error(f"Unexpected error during updating user: {str(e)}")
            return {'error': 'An unexpected error occurred. Please try again later.'}, 500
