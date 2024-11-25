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
    GET /api/v1/users/email/<email> : Get a user by their email (Non-admin).
"""


from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request
from app.services import facade
from werkzeug.exceptions import BadRequest, Forbidden, NotFound
from flask import current_app


api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user'),
    'is_admin': fields.Boolean(required=False, default=False, description='Is the user an admin')  # Ajout du champ isAdmin
    })


user_update_model = api.model('UserUpdate', {
    'first_name': fields.String(description='First name of the user'),
    'last_name': fields.String(description='Last name of the user'),
    'email': fields.String(description='Email of the user (unique)'),
    'password': fields.String(description='New password for the user'),
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

        current_app.logger.info(f"Received user data: {user_data}")

        if facade.get_user_by_email(user_data['email']):
            raise BadRequest('Email already registered')

        try:
            new_user = facade.create_user(user_data)
            return {
                'message': 'User created successfully',
                'user_id': new_user.id,
            }, 201
        except Exception as e:
            current_app.logger.error(f"Error during user creation: {e}")
            raise BadRequest('An unexpected error occurred. Please try again later.')

# -------------------------- Retrieve User by Email --------------------------

@api.route('/users/email/<email>')
class UserByEmail(Resource):
    @api.doc(description='Retrieve a user\'s details by email.')
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, email):
        """
        Retrieve a user's details by email.
        """
        user = facade.get_user_by_email(email)
        if not user:
            raise NotFound('User not found')
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        }, 200

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
            raise Forbidden('Admin privileges required')

        user_data = request.json
        email = user_data.get('email')
        if facade.get_user_by_email(email):
            raise BadRequest('Email already registered')

        try:
            new_user = facade.create_user(user_data)
            return {
                'message': 'User created successfully',
                'user_id': new_user.id,
            }, 201
        except Exception:
            raise BadRequest('An unexpected error occurred. Please try again later.')

@api.route('/admin/users/<user_id>')
class AdminUserModify(Resource):
    @jwt_required()
    @api.doc(description='Update User (admin)', security='BearerAuth')
    @api.expect(user_update_model, validate=True)
    @api.response(200, 'User successfully updated')
    @api.response(400, 'Email already in use')
    @api.response(403, 'Admin privileges required')
    def put(self, user_id):
        """
        Modify an existing user's data (Admin only).
        Admins can update any user, including email and password.
        """
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            raise Forbidden('Admin privileges required')

        data = request.json
        if 'email' in data:
            existing_user = facade.get_user_by_email(data['email'])
            if existing_user and existing_user.id != user_id:
                raise BadRequest('Email already in use')

        updated_user = facade.update_user(user_id, data)
        return {'message': 'User updated successfully', 'user_id': updated_user.id}, 200

# -------------------------- Non-Admin Routes --------------------------

@api.route('/users/<user_id>')
class UserResource(Resource):
    @api.doc(description='Retrieve User by ID')
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """
        Retrieve a user's details by ID.
        """
        user = facade.get_user(user_id)
        if not user:
            raise NotFound('User not found')
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            }, 200

    @jwt_required() # add SD
    @api.doc(description='Update User by ID', security='BearerAuth')
    @api.response(200, 'User successfully updated')
    @api.response(403, 'Unauthorized action')
    @api.response(400, 'Invalid input data')
    def put(self, user_id):
        """
        Update a user's details by ID.
        """
        current_user = get_jwt_identity()
        if str(current_user['id']) != str(user_id):
            raise Forbidden('Unauthorized action')

        user_data = request.json
        if 'email' in user_data or 'password' in user_data:
            raise BadRequest('You cannot modify email or password')

        updated_user = facade.update_user(user_id, user_data)
        if not updated_user:
            raise NotFound('User not found')

        return {
            'id': updated_user.id,
            'first_name': updated_user.first_name,
            'last_name': updated_user.last_name,
            'email': updated_user.email,
        }, 200


# -------------------------- List All Users (Admin Only) --------------------------

@api.route('/admin/users')
class AdminUserList(Resource):
    @jwt_required()
    @api.doc(description='Retrieve all user (admin)', security='BearerAuth')
    @api.response(200, 'List of users retrieved successfully')
    @api.response(403, 'Admin privileges required')
    def get(self):
        """
        Get a list of all users (Admin only).
        Admins can view the list of all users.
        """
        current_app.logger.info(f"Request headers: {request.headers}")
        current_user = get_jwt_identity()
        current_app.logger.info(f"Current user: {current_user}")

        if not current_user.get('is_admin'):
            raise Forbidden('Admin privileges required')

        users = facade.get_all_users()
        if not users:
            raise NotFound('No users found')

        return [
            {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
            }
            for user in users
        ], 200
