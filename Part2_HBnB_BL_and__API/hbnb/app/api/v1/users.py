#!/usr/bin/python3

# app/api/v1/users.py
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
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
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
        """Get the list of users"""
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
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
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
        """Update user details"""
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
