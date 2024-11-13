from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

# Create a Namespace for the API version
api = Namespace('protected', description='Protected resources')

# Define the protected endpoint
@api.route('/protected')
class ProtectedResource(Resource):
    @jwt_required()  # Protects this route with JWT authentication
    def get(self):
        """A protected endpoint that requires a valid JWT token"""
        current_user = get_jwt_identity()  # Get user identity (payload) from the JWT
        return {'message': f'Hello, user {current_user["id"]}'}, 200
