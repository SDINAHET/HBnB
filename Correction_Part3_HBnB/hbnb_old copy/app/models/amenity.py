from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.facade import HBnBFacade

api = Namespace('amenities', description='Amenities-related operations')

# Define input model for creating or updating amenities
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

facade = HBnBFacade()


@api.route('/')
class AmenityList(Resource):
    @api.doc('list_amenities')
    def get(self):
        """List all amenities"""
        amenities = facade.get_all_amenities()
        return jsonify([amenity.to_dict() for amenity in amenities])

    @api.expect(amenity_model)
    @jwt_required()
    def post(self):
        """Create a new amenity (admin only)"""
        current_user = get_jwt_identity()
        if not current_user.get('is_admin', False):
            return {'error': 'Admin privileges required'}, 403

        amenity_data = request.json
        try:
            new_amenity = facade.create_amenity(amenity_data)
            return jsonify(new_amenity.to_dict()), 201
        except ValueError as e:
            return {'error': str(e)}, 400


@api.route('/<string:amenity_id>')
class AmenityDetail(Resource):
    @api.doc('get_amenity')
    def get(self, amenity_id):
        """Get a specific amenity by ID"""
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': 'Amenity not found'}, 404
        return jsonify(amenity.to_dict())

    @api.expect(amenity_model)
    @jwt_required()
    def put(self, amenity_id):
        """Update an amenity (admin only)"""
        current_user = get_jwt_identity()
        if not current_user.get('is_admin', False):
            return {'error': 'Admin privileges required'}, 403

        amenity_data = request.json
        try:
            updated_amenity = facade.update_amenity(amenity_id, amenity_data)
            return jsonify(updated_amenity.to_dict())
        except ValueError as e:
            return {'error': str(e)}, 400
        except KeyError as e:
            return {'error': f'Missing field: {str(e)}'}, 400

    @api.doc('delete_amenity')
    @jwt_required()
    def delete(self, amenity_id):
        """Delete an amenity (admin only)"""
        current_user = get_jwt_identity()
        if not current_user.get('is_admin', False):
            return {'error': 'Admin privileges required'}, 403

        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': 'Amenity not found'}, 404

        facade.delete_amenity(amenity_id)
        return {'message': 'Amenity deleted successfully'}, 200
