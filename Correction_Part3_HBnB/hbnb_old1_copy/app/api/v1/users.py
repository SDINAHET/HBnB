from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User
from app.services.facade import HBnBFacade

api = Namespace('users', description='User-related operations')

# Define input model for creating or updating users
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password for the user')
})

update_model = api.model('UserUpdate', {
    'first_name': fields.String(description='First name of the user'),
    'last_name': fields.String(description='Last name of the user')
})

facade = HBnBFacade()

@api.route('/')
class UserList(Resource):
    @api.doc('list_users')
    @jwt_required()
    def get(self):
        """List all users (admin only)"""
        current_user = get_jwt_identity()
        if not current_user.get('is_admin', False):
            return {'error': 'Admin privileges required'}, 403

        users = facade.get_all_users()
        return jsonify([user.to_dict() for user in users])

    @api.expect(user_model)
    @jwt_required()
    def post(self):
        """Create a new user (admin only)"""
        current_user = get_jwt_identity()
        if not current_user.get('is_admin', False):
            return {'error': 'Admin privileges required'}, 403

        user_data = request.json
        try:
            new_user = facade.create_user(user_data)
            return jsonify(new_user.to_dict()), 201
        except ValueError as e:
            return {'error': str(e)}, 400


@api.route('/<string:user_id>')
class UserDetail(Resource):
    @api.doc('get_user')
    @jwt_required()
    def get(self, user_id):
        """Get a user by ID (admin only)"""
        current_user = get_jwt_identity()
        if not current_user.get('is_admin', False):
            return {'error': 'Admin privileges required'}, 403

        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return jsonify(user.to_dict())

    @api.expect(update_model)
    @jwt_required()
    def put(self, user_id):
        """Update user details (self or admin)"""
        current_user = get_jwt_identity()
        if not current_user.get('is_admin', False) and current_user['id'] != user_id:
            return {'error': 'Unauthorized action'}, 403

        update_data = request.json
        try:
            updated_user = facade.update_user(user_id, update_data)
            return jsonify(updated_user.to_dict())
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.doc('delete_user')
    @jwt_required()
    def delete(self, user_id):
        """Delete a user (admin or self-deletion)"""
        current_user = get_jwt_identity()
        if not current_user.get('is_admin', False) and current_user['id'] != user_id:
            return {'error': 'Unauthorized action'}, 403

        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        facade.delete_user(user_id)
        return {'message': 'User deleted successfully'}, 200
