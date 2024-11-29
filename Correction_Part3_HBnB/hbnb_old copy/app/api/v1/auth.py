from flask import jsonify, request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.services.facade import HBnBFacade
from werkzeug.security import check_password_hash

api = Namespace('auth', description='Authentication operations')

# Login model for API documentation
login_model = api.model('Login', {
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user')
})

# Instantiate the Facade
facade = HBnBFacade()

@api.route('/login')
class Login(Resource):
    @api.doc('user_login')
    @api.expect(login_model, validate=True)
    def post(self):
        """Authenticate a user and return an access token"""
        data = request.get_json()

        # Validate input
        email = data.get('email')
        password = data.get('password')
        if not email or not password:
            return {'error': 'Email and password are required'}, 400

        # Authenticate user
        user = facade.get_user_by_email(email)
        if not user or not check_password_hash(user.password, password):
            return {'error': 'Invalid email or password'}, 401

        # Create JWT token
        token = create_access_token(identity={
            'id': user.id,
            'email': user.email,
            'is_admin': user.is_admin
        })

        return jsonify({'access_token': token}), 200


@api.route('/profile')
class Profile(Resource):
    @api.doc('get_profile')
    @jwt_required()
    def get(self):
        """Retrieve the profile of the logged-in user"""
        user_identity = get_jwt_identity()
        user = facade.get_user_by_id(user_identity['id'])
        if not user:
            return {'error': 'User not found'}, 404

        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'is_admin': user.is_admin
        }, 200
