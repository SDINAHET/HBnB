
from flask_restx import Resource, fields
from . import places as api

place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title'),
    'price': fields.Float(required=True, description='Price'),
    'latitude': fields.Float(required=True, description='Latitude'),
    'longitude': fields.Float(required=True, description='Longitude'),
    'owner_id': fields.String(required=True, description='Owner ID')
})

@api.route('/')
class PlaceList(Resource):
    def get(self):
        return [], 200
    def post(self):
        return {"message": "Place created"}, 201
    