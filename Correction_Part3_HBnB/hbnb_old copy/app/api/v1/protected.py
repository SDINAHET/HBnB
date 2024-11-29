from flask import jsonify
from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.facade import HBnBFacade

api = Namespace('protected', description='Protected operations requiring authentication')

# Instantiate the Facade
facade = HBnBFacade()

@api.route('/admin')
class AdminOnlyResource(Resource):
    @api.doc('admin_access')
    @jwt_required()
    def get(self):
        """Admin-only access"""
        current_user = get_jwt_identity()
        if not current_user.get('is_admin', False):
            return {'error': 'Admin privileges required'}, 403
        return {'message': 'Welcome, admin!'}

@api.route('/user-details')
class UserDetailsResource(Resource):
    @api.doc('user_details')
    @jwt_required()
    def get(self):
        """Retrieve details of the currently authenticated user"""
        current_user = get_jwt_identity()
        user = facade.get_user_by_id(current_user['id'])
        if not user:
            return {'error': 'User not found'}, 404
        return jsonify({
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'is_admin': user.is_admin
        })
