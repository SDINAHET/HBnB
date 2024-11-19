
from flask_restx import Resource, fields
from . import amenities as api

amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Amenity name')
})

@api.route('/')
class AmenityList(Resource):
    def get(self):
        return [], 200
    def post(self):
        return {"message": "Amenity created"}, 201
    