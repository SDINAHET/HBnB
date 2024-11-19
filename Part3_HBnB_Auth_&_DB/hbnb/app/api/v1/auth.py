#!/usr/bin/python3

from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.services import facade

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
    def post(self):
        """
        Authenticate user and return a JWT token
        """
        credentials = api.payload

        user = facade.get_user_by_email(credentials['email'])

        if not user:
            return {'error': 'User not found'}, 404
        if not user.verify_password(credentials['password']):
            return {'error': 'Invalid credentials'}, 401
        
        access_token = create_access_token(identity={'id': str(user.id), 'is_admin': user.is_admin})
        return {'access_token': access_token}, 200
