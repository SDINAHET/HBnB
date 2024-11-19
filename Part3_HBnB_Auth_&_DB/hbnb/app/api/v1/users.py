#!/usr/bin/python3
"""
This module defines the API endpoints for user management in the HBnB application.
It implements the routes for creating, retrieving, and updating users.

Routes:
    POST /api/v1/users/ : Create a new user (Non-admin).
    POST /api/v1/admin/users/ : Create a new user (Admin only).
    GET /api/v1/users/<user_id> : Get a specific user by ID.
    PUT /api/v1/users/<user_id> : Update a user's information.
    GET /api/v1/admin/users/ : Get the list of all users (Admin only).
"""


from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity #add SD
from flask import request
from app.services import facade


api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user'),
    'is_admin': fields.Boolean(required=False, default=False, description='Is the user an admin')  # Ajout du champ isAdmin
    })

# -------------------------- Non-Admin User Creation --------------------------

@api.route('/users/')
class UserCreate(Resource):
    @api.expect(user_model, validate=True)
    @api.doc(description='Register a new user (accessible to anyone).')
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    def post(self):
        """
        Register a new user.
        Accessible to anyone (non-authenticated users).
        """
        user_data = request.json

        if facade.get_user_by_email(user_data['email']):
            return {'error': 'Email already registered'}, 400

        try:
            new_user = facade.create_user(user_data)
            return {
                'message': 'User created successfully',
                'user_id': new_user.id,
            }, 201
        except Exception as e:
            return {'error': 'An unexpected error occurred. Please try again later.'}, 500

# -------------------------- Admin Routes --------------------------

@api.route('/admin/users/')
class AdminUserCreate(Resource):
    @jwt_required()
    def post(self):
        """
        Create a new user (Admin only).
        Admins can create users and validate their email uniqueness.
        """
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        user_data = request.json
        email = user_data.get('email')
        if facade.get_user_by_email(email):
            return {'error': 'Email already registered'}, 400

        try:
            new_user = facade.create_user(user_data)
            return {
                'message': 'User created successfully',
                'user_id': new_user.id,
            }, 201
        except Exception as e:
            return {'error': 'An unexpected error occurred. Please try again later.'}, 500

@api.route('/admin/users/<user_id>')
class AdminUserModify(Resource):
    @jwt_required()
    def put(self, user_id):
        """
        Modify an existing user's data (Admin only).
        Admins can update any user, including email and password.
        """
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        data = request.json
        email = data.get('email')
        if email:
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email aready in use'}, 400

        updated_user = facade.update_user(user_id, data)
        return {'message': 'User updated successfully', 'user_id': updated_user.id}, 200

# -------------------------- Non-Admin Routes --------------------------

@api.route('/users/<user_id>')
class UserResource(Resource):
    """
    Resource class for handling individual user operations: retrieval and update.

    Methods:
        get: Retrieves a specific user by their ID.
        put: Updates a user's information.
    """

    @api.doc(description='Retrieve a user''s details by ID.')
    @api.doc(params={'user_id': 'The ID of the user to retrieve'})
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """
        Retrieve a user's details by ID.
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

    @api.doc(description='Update a user''s details by ID.')
    @api.doc(params={'user_id': 'The ID of the user to update'})
    @jwt_required() # add SD
    @api.expect(user_model, validate=True)
    @api.response(200, 'User successfully updated')
    @api.response(403, 'Unauthorized action')
    @api.response(404, 'User not found')
    @api.response(400, 'Invalid input data')
    def put(self, user_id):
        """
        Update a user's details by ID.
        """
        current_user = get_jwt_identity()

        if str(current_user['id']) != str(user_id):
            return {'error': 'Unauthorized action'}, 403

        user_data = api.payload

        if 'email' in user_data or 'password' in user_data:
            return {'error': 'You cannot modify email or password'}, 400

        try:
            updated_user = facade.update_user(user_id, user_data)
            if not updated_user:
                return {'error': 'User not found'}, 404

            return {
                'id': updated_user.id,
                'first_name': updated_user.first_name,
                'last_name': updated_user.last_name,
                'email': updated_user.email,
            }, 200

        except ValueError as e: # add SD
            return {'error': str(e)}, 400 # add SD
        except Exception as e:
            return {'error': 'An unexpected error occurred. Please try again later.'}, 500

# -------------------------- List All Users (Admin Only) --------------------------

@api.route('/admin/users')
class AdminUserList(Resource):
    @jwt_required()
    def get(self):
        """
        Get a list of all users (Admin only).
        Admins can view the list of all users.
        """
        current_user = jwt_required()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        users = facade.get_all_users()
        if not users:
            return {'error': 'No users found'}, 404

        return [{
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        } for user in users], 200


# @api.route('/')
# class UserList(Resource):
#     """
#     Resource class for handling user creation and retrieval of all users.

#     Methods:
#         post: Registers a new user.
#         get: Retrieves a list of all users.
#     """

#     @api.expect(user_model, validate=True)
#     @api.doc(description='Register a new user')  # Description de l'action dans Swagger
#     @api.response(201, 'User successfully created')
#     @api.response(400, 'Email already registered')
#     @api.response(400, 'Invalid input data')
#     def post(self):
#         """
#         Register a new user.
#         -------------------

#         This method handles the registration of a new user, checks for email uniqueness, and returns the user details if successfully created.
#         --------------------------------------------------------------------------------

#         Returns:
#         --------
#         tuple: A tuple containing:
#             - dict: A dictionary with the new user's details.
#                 - `id` (str): The user's ID.
#                 - `first_name` (str): The user's first name.
#                 - `last_name` (str): The user's last name.
#                 - `email` (str): The user's email.
#             - int: The HTTP status code (201 on success, 400 on failure).

#         Raises:
#         -------
#         ValidationError: If input data fails validation checks.
#         ValueError: If the email is already registered.
#         """

#         user_data = api.payload

#         existing_user = facade.get_user_by_email(user_data['email'])
#         if existing_user:
#             return {'error': 'Email already registered'}, 400

#         try:
#             new_user = facade.create_user(user_data)
#             new_user.hash_password(user_data['password'])
#             return {
#                 'id': new_user.id,
#                 'first_name': new_user.first_name,
#                 'last_name': new_user.last_name,
#                 'email': new_user.email,
#             }, 201
#         except ValidationError as ve:  # a modifié except ValueError as e:
#             return {'error': ve.messages}, 400
#         except Exception as e:
#             return {'error': str(e)}, 400

#     @api.doc(description='Retrieve the list of all users.')
#     @api.response(200, 'List of users retrieved successfully')
#     @api.response(404, 'No users found')
#     def get(self):
#         """
#         Retrieve the list of all users.
#         -------------------------------

#         This method retrieves all registered users. If no users are found, a 404 error is returned.
#         --------------------------------------------------------------------------------------------

#         Returns:
#         --------
#         tuple: A tuple containing:
#             - list: A list of dictionaries with user details.
#                 - `id` (str): The user's ID.
#                 - `first_name` (str): The user's first name.
#                 - `last_name` (str): The user's last name.
#                 - `email` (str): The user's email.
#             - int: The HTTP status code (200 on success, 404 on failure).
#         """
#         users = facade.get_all_users()
#         if not users:
#             return {'error': 'No users found'}, 404
#         return [{
#             'id': user.id,
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#             'email': user.email,
#             } for user in users], 200
