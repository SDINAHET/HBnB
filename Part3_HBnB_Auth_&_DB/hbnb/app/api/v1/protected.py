from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request

# Create a Namespace for the protected resources
api = Namespace('protected', description='Protected resources')

@api.route('/protected')
class ProtectedResource(Resource):
    """
    Resource for handling protected operations, requiring authentication with JWT.
    """
    @jwt_required()
    @api.doc(description='A protected endpoint that requires a valid JWT token', security='Bearer Auth')
    @api.response(200, 'Success')
    @api.response(401, 'Unauthorized')
    def get(self):
        """
        Retrieve a protected resource, requiring the client to include a valid JWT token.

        Returns:
        --------
        dict: A JSON object containing a personalized message for the current user based on
              the ID extracted from the JWT token.

        Status Code:
        ------------
        200: Request was successful.
        401: Unauthorized - Missing or invalid token.
        """
        current_user = get_jwt_identity()  # Get user identity (payload) from the JWT
        return {'message': f'Hello, user {current_user}'}, 200
