# hbnb/app/api/v1/routes/places.py

from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade
from flask_jwt_extended import jwt_required, get_jwt_identity

# Namespace for places
api = Namespace("places", description="Operations related to places")

# Place model for API documentation
place_model = api.model(
    "Place",
    {
        "id": fields.String(readonly=True, description="Unique identifier of the place"),
        "title": fields.String(required=True, description="Title of the place"),
        "description": fields.String(description="Description of the place"),
        "price": fields.Float(required=True, description="Price per night"),
        "latitude": fields.Float(required=True, description="Latitude of the location"),
        "longitude": fields.Float(required=True, description="Longitude of the location"),
        "owner_id": fields.String(readonly=True, description="ID of the place owner"),
    },
)

# Instantiate the Facade
facade = HBnBFacade()


@api.route("/")
class PlaceList(Resource):
    @api.doc("get_all_places")
    @api.marshal_list_with(place_model)
    def get(self):
        """Retrieve all places"""
        places = facade.get_all_places()
        return places, 200

    @api.doc("create_place")
    @api.expect(place_model, validate=True)
    @jwt_required()
    def post(self):
        """Create a new place (Owner only)"""
        user = get_jwt_identity()
        if not user:
            return {"error": "Authentication required"}, 403

        data = request.get_json()
        required_fields = ["title", "price", "latitude", "longitude"]
        for field in required_fields:
            if field not in data or not data[field]:
                return {"error": f"{field} is required"}, 400

        if not -90 <= data["latitude"] <= 90 or not -180 <= data["longitude"] <= 180:
            return {"error": "Invalid latitude or longitude"}, 400

        try:
            place = facade.create_place(data, owner_id=user["id"])
            return jsonify(place), 201
        except Exception as e:
            return {"error": str(e)}, 500


@api.route("/<string:place_id>")
class PlaceDetail(Resource):
    @api.doc("get_place_by_id")
    @api.marshal_with(place_model)
    def get(self, place_id):
        """Retrieve a specific place by ID"""
        place = facade.get_place_by_id(place_id)
        if not place:
            return {"error": "Place not found"}, 404
        return place, 200

    @api.doc("update_place")
    @api.expect(place_model, validate=True)
    @jwt_required()
    def put(self, place_id):
        """Update a specific place (Owner only)"""
        user = get_jwt_identity()
        data = request.get_json()

        try:
            updated_place = facade.update_place(place_id, data, owner_id=user["id"])
            if not updated_place:
                return {"error": "Place not found or unauthorized"}, 404
            return jsonify(updated_place), 200
        except Exception as e:
            return {"error": str(e)}, 500

    @api.doc("delete_place")
    @jwt_required()
    def delete(self, place_id):
        """Delete a specific place (Owner only)"""
        user = get_jwt_identity()
        try:
            result = facade.delete_place(place_id, owner_id=user["id"])
            if not result:
                return {"error": "Place not found or unauthorized"}, 404
            return {"message": "Place deleted successfully"}, 200
        except Exception as e:
            return {"error": str(e)}, 500
