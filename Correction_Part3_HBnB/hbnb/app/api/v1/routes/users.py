# hbnb/app/api/v1/routes/users.py

from flask import jsonify, request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.facade import HBnBFacade

# Namespace for Users
api = Namespace("users", description="Operations related to users")

# User model for API documentation
user_model = api.model(
    "User",
    {
        "id": fields.String(readonly=True, description="Unique identifier of the user"),
        "first_name": fields.String(required=True, description="First name of the user"),
        "last_name": fields.String(required=True, description="Last name of the user"),
        "email": fields.String(required=True, description="Email of the user"),
        "is_admin": fields.Boolean(
            readonly=True, description="Indicates if the user is an admin"
        ),
        "created_at": fields.String(readonly=True, description="User creation date"),
        "updated_at": fields.String(readonly=True, description="Last update date"),
    },
)

# Instantiate the Facade
facade = HBnBFacade()


@api.route("/")
class UserList(Resource):
    @api.doc("get_all_users")
    @api.marshal_list_with(user_model)
    @jwt_required()
    def get(self):
        """Retrieve all users (Admin only)"""
        user = get_jwt_identity()
        if not user.get("is_admin"):
            return {"error": "Admin privileges required"}, 403

        users = facade.get_all_users()
        return users, 200

    @api.doc("create_user")
    @api.expect(user_model, validate=True)
    def post(self):
        """Create a new user"""
        data = request.get_json()

        required_fields = ["first_name", "last_name", "email", "password"]
        for field in required_fields:
            if field not in data or not data[field]:
                return {"error": f"{field} is required"}, 400

        if len(data["first_name"]) > 50 or len(data["last_name"]) > 50:
            return {"error": "Name fields must not exceed 50 characters"}, 400

        if not "@" in data["email"] or len(data["email"]) > 255:
            return {"error": "Invalid email format or length"}, 400

        try:
            user = facade.create_user(data)
            return jsonify(user), 201
        except Exception as e:
            return {"error": str(e)}, 500


@api.route("/<string:user_id>")
class UserDetail(Resource):
    @api.doc("get_user_by_id")
    @api.marshal_with(user_model)
    @jwt_required()
    def get(self, user_id):
        """Retrieve a user by ID (Admin only)"""
        user = get_jwt_identity()
        if not user.get("is_admin"):
            return {"error": "Admin privileges required"}, 403

        user = facade.get_user_by_id(user_id)
        if not user:
            return {"error": "User not found"}, 404
        return user, 200

    @api.doc("delete_user")
    @jwt_required()
    def delete(self, user_id):
        """Delete a user (Admin only)"""
        current_user = get_jwt_identity()
        if not current_user.get("is_admin"):
            return {"error": "Admin privileges required"}, 403

        try:
            result = facade.delete_user(user_id)
            if not result:
                return {"error": "User not found"}, 404
            return {"message": "User deleted successfully"}, 200
        except Exception as e:
            return {"error": str(e)}, 500
