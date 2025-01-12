#!/usr/bin/python3

from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.services import facade
from flask import current_app

api = Namespace('auth', description='Authentication operations')

login_model = api.model('Login', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

@api.route('/login')
class Login(Resource):
    @api.doc(description='Authenticate user and return a JWT token')
    @api.expect(login_model)
    @api.response(200, 'Login successful')
    @api.response(401, 'Invalid credentials')
    @api.response(404, 'User not found')
    def post(self):
        """
        Authenticate user and return a JWT token
        """
        credentials = api.payload

        current_app.logger.info(f"User {credentials['email']} login attempt")
        user = facade.get_user_by_email(credentials['email'])

        if not user:
            current_app.logger.error(f"User not found: {credentials['email']}")
            return {'error': 'User not found'}, 404
        if not user.verify_password(credentials['password']):
            current_app.logger.error(f"Invalid credentials for user: {credentials['email']}")
            return {'error': 'Invalid credentials'}, 401

        # Créer un JWT token avec l'identité utilisateur
        access_token = create_access_token(identity={'id': str(user.id), 'is_admin': user.is_admin})

        # Retourner le token et l'ID utilisateur dans la réponse
        return {
            'access_token': access_token,
            'user_id': str(user.id)  # Inclure l'ID utilisateur
        }, 200
