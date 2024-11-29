# hbnb/app/api/v1/routes/auth.py

from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta

# Namespace for authentication
api = Namespace("auth", description="Authentication related operations")

# Input model for login
login_model = api.model(
    "Login",
    {
        "email": fields.String(required=True, description="User email"),
        "password": fields.String(required=True, description="User password"),
    },
)

# Instantiate the Facade
facade = HBnBFacade()


@api.route("/login")
class Login(Resource):
    @api.doc("login_user")
    @api.expect(login_model, validate=True)
    def post(self):
        """Login a user and return a JWT token"""
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return {"error": "Email and password are required"}, 400

        try:
            user = facade.authenticate_user(email, password)
            if not user:
                return {"error": "Invalid email or password"}, 401

            token = create_access_token(
                identity={"id": user.id, "email": user.email, "is_admin": user.is_admin},
                expires_delta=timedelta(hours=24),
            )
            return {"access_token": token, "user": {"id": user.id, "email": user.email, "is_admin": user.is_admin}}, 200
        except Exception as e:
            return {"error": str(e)}, 500


@api.route("/me")
class CurrentUser(Resource):
    @api.doc("get_current_user")
    @jwt_required()
    def get(self):
        """Get the currently authenticated user's information"""
        user = get_jwt_identity()
        return {"id": user.get("id"), "email": user.get("email"), "is_admin": user.get("is_admin")}, 200
