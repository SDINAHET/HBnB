from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.facade import HBnBFacade

api = Namespace('places', description='Operations related to places')

# Define the input/output models for API documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place')
})

place_update_model = api.model('PlaceUpdate', {
    'title': fields.String(description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(description='Price per night'),
    'latitude': fields.Float(description='Latitude of the place'),
    'longitude': fields.Float(description='Longitude of the place')
})

# Instantiate the Facade
facade = HBnBFacade()

@api.route('/')
class PlacesList(Resource):
    @api.doc('list_places')
    def get(self):
        """Get a list of all places"""
        places = facade.get_all_places()
        return jsonify([{
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'price': place.price,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner_id': place.owner_id
        }])

    @api.doc('create_place')
    @api.expect(place_model, validate=True)
    @jwt_required()
    def post(self):
        """Create a new place"""
        current_user = get_jwt_identity()
        data = request.get_json()

        # Create the place
        place = facade.create_place(
            title=data['title'],
            description=data.get('description'),
            price=data['price'],
            latitude=data['latitude'],
            longitude=data['longitude'],
            owner_id=current_user['id']
        )
        return jsonify({
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'price': place.price,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner_id': place.owner_id
        }), 201


@api.route('/<string:place_id>')
class PlaceDetail(Resource):
    @api.doc('get_place')
    def get(self, place_id):
        """Get a specific place by ID"""
        place = facade.get_place_by_id(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        return jsonify({
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'price': place.price,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner_id': place.owner_id
        })

    @api.doc('update_place')
    @api.expect(place_update_model, validate=True)
    @jwt_required()
    def put(self, place_id):
        """Update a specific place"""
        current_user = get_jwt_identity()
        data = request.get_json()

        # Update the place
        place = facade.update_place(
            place_id=place_id,
            data=data,
            current_user_id=current_user['id']
        )
        if not place:
            return {'error': 'Unauthorized or place not found'}, 403
        return jsonify({
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'price': place.price,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner_id': place.owner_id
        })

    @api.doc('delete_place')
    @jwt_required()
    def delete(self, place_id):
        """Delete a specific place"""
        current_user = get_jwt_identity()
        success = facade.delete_place(place_id=place_id, current_user_id=current_user['id'])
        if not success:
            return {'error': 'Unauthorized or place not found'}, 403
        return {'message': 'Place deleted successfully'}, 200
