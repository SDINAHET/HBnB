# hbnb/app/api/v1/routes/amenities.py

from flask import jsonify, request
from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade
from flask_jwt_extended import jwt_required, get_jwt_identity

# Namespace for amenities
api = Namespace("amenities", description="Operations related to amenities")

# Amenity model for API documentation
amenity_model = api.model(
    "Amenity",
    {
        "id": fields.String(readonly=True, description="Unique identifier of the amenity"),
        "name": fields.String(required=True, description="Name of the amenity"),
    },
)

# Instantiate the Facade
facade = HBnBFacade()


@api.route("/")
class AmenityList(Resource):
    @api.doc("get_all_amenities")
    @api.marshal_list_with(amenity_model)
    def get(self):
        """Retrieve all amenities"""
        amenities = facade.get_all_amenities()
        return amenities, 200

    @api.doc("create_amenity")
    @api.expect(amenity_model, validate=True)
    @jwt_required()
    def post(self):
        """Create a new amenity (Admin only)"""
        user = get_jwt_identity()
        if not user.get("is_admin"):
            return {"error": "Admin privileges required"}, 403

        data = request.get_json()
        if "name" not in data or not data["name"]:
            return {"error": "Amenity name is required"}, 400

        if len(data["name"]) > 50:
            return {"error": "Amenity name must not exceed 50 characters"}, 400

        try:
            amenity = facade.create_amenity(data)
            return jsonify(amenity), 201
        except Exception as e:
            return {"error": str(e)}, 500


@api.route("/<string:amenity_id>")
class AmenityDetail(Resource):
    @api.doc("get_amenity_by_id")
    @api.marshal_with(amenity_model)
    def get(self, amenity_id):
        """Retrieve a specific amenity by ID"""
        amenity = facade.get_amenity_by_id(amenity_id)
        if not amenity:
            return {"error": "Amenity not found"}, 404
        return amenity, 200

    @api.doc("update_amenity")
    @api.expect(amenity_model, validate=True)
    @jwt_required()
    def put(self, amenity_id):
        """Update an amenity (Admin only)"""
        user = get_jwt_identity()
        if not user.get("is_admin"):
            return {"error": "Admin privileges required"}, 403

        data = request.get_json()
        if "name" not in data or not data["name"]:
            return {"error": "Amenity name is required"}, 400

        if len(data["name"]) > 50:
            return {"error": "Amenity name must not exceed 50 characters"}, 400

        try:
            updated_amenity = facade.update_amenity(amenity_id, data)
            if not updated_amenity:
                return {"error": "Amenity not found"}, 404
            return updated_amenity, 200
        except Exception as e:
            return {"error": str(e)}, 500

    @api.doc("delete_amenity")
    @jwt_required()
    def delete(self, amenity_id):
        """Delete an amenity (Admin only)"""
        user = get_jwt_identity()
        if not user.get("is_admin"):
            return {"error": "Admin privileges required"}, 403

        try:
            result = facade.delete_amenity(amenity_id)
            if not result:
                return {"error": "Amenity not found"}, 404
            return {"message": "Amenity deleted successfully"}, 200
        except Exception as e:
            return {"error": str(e)}, 500
