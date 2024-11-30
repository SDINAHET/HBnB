# hbnb/app/api/v1/routes/reviews.py

from flask import jsonify, request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.facade import HBnBFacade
from sqlalchemy import CheckConstraint

# Namespace for Reviews
api = Namespace("reviews", description="Operations related to reviews")

# Review model for API documentation
review_model = api.model(
    "Review",
    {
        "id": fields.String(readonly=True, description="Unique identifier of the review"),
        "text": fields.String(required=True, description="Content of the review"),
        "rating": fields.Integer(
            required=True, description="Rating between 1 and 5"
        ),
        "user_id": fields.String(readonly=True, description="ID of the user"),
        "place_id": fields.String(readonly=True, description="ID of the place"),
    },
)

# Instantiate the Facade
facade = HBnBFacade()


@api.route("/")
class ReviewList(Resource):
    @api.doc("get_all_reviews")
    @api.marshal_list_with(review_model)
    def get(self):
        """Retrieve all reviews"""
        reviews = facade.get_all_reviews()
        return reviews, 200

    @api.doc("create_review")
    @api.expect(review_model, validate=True)
    @jwt_required()
    def post(self):
        """Create a new review"""
        user = get_jwt_identity()
        data = request.get_json()

        if not data.get("place_id"):
            return {"error": "Place ID is required"}, 400
        if not data.get("text"):
            return {"error": "Review text is required"}, 400
        if not isinstance(data.get("rating"), int) or not (1 <= data["rating"] <= 5):
            return {"error": "Rating must be an integer between 1 and 5"}, 400

        try:
            review = facade.create_review(user["id"], data)
            return jsonify(review), 201
        except Exception as e:
            return {"error": str(e)}, 500


@api.route("/<string:review_id>")
class ReviewDetail(Resource):
    @api.doc("get_review_by_id")
    @api.marshal_with(review_model)
    def get(self, review_id):
        """Retrieve a specific review by ID"""
        review = facade.get_review_by_id(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        return review, 200

    @api.doc("update_review")
    @api.expect(review_model, validate=True)
    @jwt_required()
    def put(self, review_id):
        """Update a specific review by ID"""
        user = get_jwt_identity()
        data = request.get_json()

        try:
            review = facade.update_review(review_id, user["id"], data)
            if not review:
                return {"error": "Review not found or not authorized"}, 404
            return jsonify(review), 200
        except Exception as e:
            return {"error": str(e)}, 500

    @api.doc("delete_review")
    @jwt_required()
    def delete(self, review_id):
        """Delete a specific review by ID"""
        user = get_jwt_identity()

        try:
            result = facade.delete_review(review_id, user["id"])
            if not result:
                return {"error": "Review not found or not authorized"}, 404
            return {"message": "Review deleted successfully"}, 200
        except Exception as e:
            return {"error": str(e)}, 500
