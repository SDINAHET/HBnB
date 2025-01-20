from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request # add SD
import jwt # add SD

# Create a Namespace for the API version
api = Namespace('protected', description='Protected resources')

# Define the protected endpoint
@api.route('/protected')
class ProtectedResource(Resource):
    @jwt_required()  # Protects this route with JWT authentication
    @api.doc(description='A protected endpoint that requires a valid JWT token', security='BearerAuth')
    @api.doc(security='Bearer Auth')
    @api.doc(params={'Authorization': 'A valid JWT token    --> input here: Bearer <token>'})
    @api.response(200, 'Success')
    @api.response(401, 'Unauthorized')
    def get(self):
        # """A protected endpoint that requires a valid JWT token"""
        """
        A protected endpoint that requires a valid JWT token
        -----------------------------------------------------

        This method is used to retrieve a protected resource, requiring the client to include a valid JSON Web Token (JWT) in the request's authorization header. The token's identity is extracted to identify the current user.
        -----------------------------------------------------------------------------------------------------

        Parameters:
        -----------
        self : ProtectedResource
            The instance of the ProtectedResource class on which this method is called.

        Raises:
        -------
        jwt.exceptions.NoAuthorizationError
            If the request does not contain a valid JWT token.
        jwt.exceptions.JWTDecodeError
            If the token is malformed or cannot be decoded.
        jwt.exceptions.ExpiredSignatureError
            If the token has expired.
        jwt.exceptions.InvalidTokenError
            If the token is invalid for any other reason.

        Returns:
        --------
        dict
            A JSON object containing a personalized message for the current user based on
            the ID extracted from the JWT token.

        int
            The HTTP status code (200) indicating that the request was successful.

        Raises:
        -------
        401 Unauthorized

        Example:
        --------
        When a user accesses this endpoint with a valid JWT token:

        ```json
        {
            "message": "Hello, user 12345"
        }
        ```
        """
        # Récupération du token JWT depuis l'en-tête Authorization
        # auth_header = request.headers.get('Authorization')

        # if not auth_header:
        #     return {'msg': 'Missing Authorization Header'}, 401

        # try:
        #     current_user = get_jwt_identity()  # Get user identity (payload) from the JWT
        #     # Le token doit être dans la forme 'Bearer <token>'
        #     # token = auth_header.split(' ')[1]
        #     # Décodez et vérifiez le token
        #     # decoded_token = jwt.decode(token, 'secret_key', algorithms=['HS256'])
        #     # user_id = decoded_token.get('sub')

        #     # Ici, vous pouvez ajouter de la logique pour récupérer un message personnalisé pour l'utilisateur
        #     #return {'message': f"Hello, user {user_id}"}, 200
        #     return {'message': f'Hello, user {current_user["id"]}'}, 200

        # except jwt.ExpiredSignatureError:
        #     return {'msg': 'Token has expired'}, 401
        # except jwt.InvalidTokenError:
        #     return {'msg': 'Invalid token'}, 401
        # except IndexError:
        #     return {'msg': 'Token malformed'}, 401
        # auth_header = request.headers.get('Authorization')
        # current_app.logger.info(f"Authorization Header: {auth_header}")
        # current_user = get_jwt_identity()  # Get user identity (payload) from the JWT
        # return {'message': f'Hello, user {current_user["id"]}'}, 200

        # Vérifiez si le token est dans l'en-tête ou dans l'URL
        # auth_header = request.headers.get('Authorization')
        # token_from_url = request.args.get('Authorization')

        # if auth_header:
        #     # Si le token est dans l'en-tête, utilisez-le
        #     verify_jwt_in_request()
        # elif token_from_url:
        #     # Si le token est dans l'URL, simulez l'en-tête `Authorization`
        #     request.headers = {**request.headers, 'Authorization': f'Bearer {token_from_url}'}
        #     verify_jwt_in_request()
        # else:
        #     # Aucun token trouvé
        #     return {'msg': 'Missing Authorization Header or Token in URL'}, 401

        # auth_header = request.headers.get('Authorization')
        # current_app.logger.info(f"Authorization Header: {auth_header}")
        current_user = get_jwt_identity()
        return {'message': f'Hello, user {current_user["id"]}'}, 200

        # Récupérez l'identité de l'utilisateur
        # current_user = get_jwt_identity()
        # return {'message': f'Hello, user {current_user["id"]}'}, 200


        # try:
        #     # Récupérer l'utilisateur actuel depuis le token JWT
        #     current_user = get_jwt_identity()
        #     return {'message': f'Hello, user {current_user["id"]}'}, 200
        # except Exception as e:
        #     return {'message': 'Error processing request', 'error': str(e)}, 500


# authentification token JWT OK avec curl
# curl -X 'GET' \
#   'http://localhost:5000/api/v1/protected' \
#   -H 'accept: application/json' \
#   -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczMTU1MjUxMCwianRpIjoiMmI3MDg5ZjktMTA4ZS00YTUwLWIyYzItNDJmNDQ2MmZhYTlkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6IjhhYjdjMjI3LTdiYjQtNGQ1Ny1hZGEwLTMwMDU1ZWE4YjE2OCIsImlzX2FkbWluIjpmYWxzZX0sIm5iZiI6MTczMTU1MjUxMCwiY3NyZiI6IjAyNTdlZjkyLTc4NmUtNGZlYy05MmUwLTE3ZDMxNzc5ODJlMyIsImV4cCI6MTczMTU1MzQxMH0.V5X5eDJCD3zibLqb3oO0MBXP7h8Nsee9Jd8dLzngCgQ'

# root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/HBnB/HBnB/Part3_HBnB_Auth_&_DB/hbnb/app# c
# url -X 'GET' \
#   'http://localhost:5000/api/v1/protected' \
#   -H 'accept: application/json' \
#   -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczMTU1MjUxMCwianRpIjoiMmI3MDg5ZjktMTA4ZS00YTUwLWIyYzItNDJmNDQ2MmZhYTlkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6IjhhYjdjMjI3LTdiYjQtNGQ1Ny1hZGEwLTMwMDU1ZWE4YjE2OCIsImlzX2FkbWluIjpmYWxzZX0sIm5iZiI6MTczMTU1MjUxMCwiY3NyZiI6IjAyNTdlZjkyLTc4NmUtNGZlYy05MmUwLTE3ZDMxNzc5ODJlMyIsImV4cCI6MTczMTU1MzQxMH0.V5X5eDJCD3zibLqb3oO0MBXP7h8Nsee9Jd8dLzngCgQ'
# {
#     "message": "Hello, user 8ab7c227-7bb4-4d57-ada0-30055ea8b168"
# }
# root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/HBnB/HBnB/Part3_HBnB_
# Auth_&_DB/hbnb/app#
#
#
#
#
#root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/HBnB/HBnB# curl -X 'GET' \
#   'http://127.0.0.1:5000/api/v1/protected/protected?Authorization=Bearer%20eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczNzExNTAzMiwianRpIjoiMmFlMmZjYTItZDdlMS00NWU5LWI1ZTUtNDJjYjFhY2FmYTQ3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6ImZmN2I5NzM0LTVhYWQtNDk1Ni05NTAzLWE2OTA1MTZlMDY2MSIsImlzX2FkbWluIjpmYWxzZX0sIm5iZiI6MTczNzExNTAzMiwiZXhwIjoxNzM3MTE1OTMyfQ.z5l9MT74k7bdbvxcl78bfy2N7zYiZUV_FHrLKmZCvTI' \
#   -H 'accept: application/json'
# {
#   "msg": "Missing Authorization Header"
# }
# root@UID7E:/mnt/c/Users/steph/Documents/2ème trimestre holberton/HBnB/HBnB# curl -X GET \
#   'http://127.0.0.1:5000/api/v1/protected/protected' \
#   -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczNzExNTAzMiwianRpIjoiMmFlMmZjYTItZDdlMS00NWU5LWI1ZTUtNDJjYjFhY2FmYTQ3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6ImZmN2I5NzM0LTVhYWQtNDk1Ni05NTAzLWE2OTA1MTZlMDY2MSIsImlzX2FkbWluIjpmYWxzZX0sIm5iZiI6MTczNzExNTAzMiwiZXhwIjoxNzM3MTE1OTMyfQ.z5l9MT74k7bdbvxcl78bfy2N7zYiZUV_FHrLKmZCvTI' \
#   -H 'accept: application/json'
# {
#     "message": "Hello, user ff7b9734-5aad-4956-9503-a690516e0661"
# }

