
from flask_restx import Resource, fields
from . import users as api

user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name'),
    'last_name': fields.String(required=True, description='Last name'),
    'email': fields.String(required=True, description='Email'),
})

@api.route('/')
class UserList(Resource):
    def get(self):
        return [], 200
    def post(self):
        return {"message": "User created"}, 201
    