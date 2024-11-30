# hbnb/app/api/v1/routes/protected.py

from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

# Namespace for protected routes
api = Namespace("protected", description="Protected operations requiring authentication")


@api.route("/")
class ProtectedResource(Resource):
    @api.doc("protected_route")
    @jwt_required()
    def get(self):
        """Example protected route that requires authentication"""
        current_user = get_jwt_identity()
        return {"message": f"Welcome, {current_user['email']}! You are authenticated."}, 200


@api.route("/admin")
class AdminProtectedResource(Resource):
    @api.doc("admin_protected_route")
    @jwt_required()
    def get(self):
        """Example protected route for admin users"""
        current_user = get_jwt_identity()
        if not current_user.get("is_admin", False):
            return {"error": "Admin privileges required"}, 403

        return {"message": f"Welcome Admin, {current_user['email']}!"}, 200
