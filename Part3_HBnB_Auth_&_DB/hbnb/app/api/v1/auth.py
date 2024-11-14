from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.services import facade

api = Namespace('auth', description='Authentication operations')

login_model = api.model('Login', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

@api.route('/login')
class Login(Resource):
    @api.doc(description='Authenticate user and return a JWT token')
    # @api.doc(params={'credentials': 'User credentials'})
    @api.expect(login_model)
    @api.response(200, 'Login successful')
    @api.response(401, 'Invalid credentials')
    def post(self):
        #"""Authenticate user and return a JWT token"""
        """
        Authenticate user and return a JWT token
        -----------------------------------------

        This method handles user authentication by verifying the provided email and password credentials. If the credentials are valid, it generates a JSON Web Token (JWT) that the user can use to access protected endpoints.
        -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        Parameters:
        -----------
        self : `Login`
        The instance of the Login resource class on which this method is called.

        Raises:
        -------
        401 Unauthorized
            If the provided `email` or `password` is invalid.

        Returns:
        --------
        dict
            A JSON object containing the `JWT access token` if authentication is successful.

        int
            The HTTP status code (200) if the login is successful, or (401) if the login fails.

        Example:
        --------
        A client can authenticate by sending a POST request with a JSON payload including
        the user's email and password. For example:

        Request Payload:
        ```json
        {
            "email": "john.doe@example.com",
            "password": "secure_password"
        }
        ```

        If the credentials are correct, the response will contain an access token:
        ```json
        {
            "access_token": "your_generated_jwt_token"
        }
        ```
        """
        credentials = api.payload

        user = facade.get_user_by_email(credentials['email'])
        if not user or not user.verify_password(credentials['password']):
            return {'error': 'Invalid credentials'}, 401

        access_token = create_access_token(identity={'id': str(user.id), 'is_admin': user.is_admin})
        return {'access_token': access_token}, 200
