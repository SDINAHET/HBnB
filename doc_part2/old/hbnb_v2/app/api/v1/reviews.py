
from flask_restx import Resource, fields
from . import reviews as api

review_model = api.model('Review', {
    'text': fields.String(required=True, description='Review text'),
    'rating': fields.Integer(required=True, description='Rating')
})

@api.route('/')
class ReviewList(Resource):
    def get(self):
        return [], 200
    def post(self):
        return {"message": "Review created"}, 201
    