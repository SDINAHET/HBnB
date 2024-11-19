from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token
from app.services import facade

api = Namespace('auth', description='Authentication operations')

# Model for input validation
login_model = api.model('Login', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    @api.response(200, 'Success')
    @api.response(401, 'Invalid credentials')
    def post(self):
        """
        Authenticate user and return a JWT token.

        Parameters:
        -----------
        - `email` (str): User's email address.
        - `password` (str): User's password.

        Returns:
        --------
        - (dict): A dictionary containing the JWT access token if credentials are valid.
        - Status code 200 if successful, 401 if invalid credentials.
        """
        credentials = api.payload  # Get the email and password from the request payload

        # Retrieve the user based on the provided email
        user = facade.get_user_by_email(credentials['email'])

        # Check if the user exists and the password is correct
        if not user or not user.verify_password(credentials['password']):
            return {'error': 'Invalid credentials'}, 401

        # Create a JWT token with the user's id and is_admin flag
        access_token = create_access_token(identity={'id': str(user.id), 'is_admin': user.is_admin})

        # Return the JWT token to the client
        return {'access_token': access_token}, 200
