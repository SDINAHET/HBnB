#!/usr/bin/python3
"""
API Endpoints for Reviews.
- Administrators have access to all functionalities (PUT, DELETE without restrictions).
- Users can only modify or delete their own reviews.
"""
import logging

from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request
from werkzeug.exceptions import BadRequest, Forbidden, NotFound
from app.services import facade

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    # 'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

review_update_model = api.model('ReviewUpdate', {
    'text': fields.String(description="New content of the review"),
    'rating': fields.Integer(description="New rating for the review (1 to 5)")
})

# --------------------- Create a Review ---------------------

# @api.route('/')
@api.route('/')
class ReviewList(Resource):
    @jwt_required()
    @api.response(201, 'Review successfully created') # 200 to 201
    @api.expect(review_model, validate=True)
    def post(self):
        """
        Create a new review.
        Accessible to authenticated users only.
        """
        # new_review_data = request.json
        # review_id = facade.create_review(new_review_data)
        # return {
        #     'message': 'Review created successfully',
        #     'review_id': review_id
        # }, 201

         # Get the currently authenticated user

        current_user = get_jwt_identity()

        # Extract data from the request
        review_data = request.json

        # Add user_id to the review data
        review_data['user_id'] = current_user.get('id')

        # Validate required fields
        required_fields = ['text', 'rating', 'place_id']
        # for field in required_fields:
        #     if field not in review_data:
        #         raise BadRequest(f"Missing required field: {field}")
        missing_fields = [field for field in required_fields if field not in review_data]
        if missing_fields:
            raise BadRequest(f"Missing required fields: {', '.join(missing_fields)}")
         # Validate the rating range
        rating = review_data.get('rating')
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise BadRequest("Rating must be an integer between 1 and 5.")

        # # Additional validation
        # if not (1 <= review_data['rating'] <= 5):
        #     raise BadRequest("Rating must be an integer between 1 and 5.")

        try:
            # Create a new review using the facade
            new_review = facade.create_review(review_data)

            # Return the created review details
            return {
                "message": "Review created successfully",
                "review_id": new_review.id,
                "text": new_review.text,
                "rating": new_review.rating,
                "place_id": new_review.place_id,
            }, 201

        # except ValueError as ve:
        #     # Handle validation errors raised by the service layer
        #     raise BadRequest(str(ve))
        # except Exception as e:
        #     # Log unexpected errors and return a generic message
        #     logging.error(f"Unexpected error while creating review: {e}")
        #     raise BadRequest("An unexpected error occurred while creating the review.")

        except Exception as e:
            # Raise a BadRequest error if any issue occurs
            raise BadRequest(str(e))

        # current_user = get_jwt_identity()
        # review_data = request.json

        # try:
        #     review_data['user_id'] = current_user.get('id')
        #     new_review = facade.create_review(review_data)
        #     return {
        #         "message": "Review created successfully",
        #         "review_id": new_review.id,
        #         "text": new_review.text,
        #         "rating": new_review.rating,
        #         "place_id": new_review.place_id,
        #     }, 201
        # except Exception as e:
        #     # traceback.print_exc()
        #     raise BadRequest(str(e))

        # except Exception as e:
        #     # Catch all other errors and print a stack trace
        #     traceback.print_exc()
        #     raise BadRequest("An internal error occurred. Please check your input.")

# --------------------- Get All Reviews ---------------------

# @api.route('/')
# class ReviewListAll(Resource):
    @jwt_required()
    def get(self):
        """
        Get all reviews.
        Accessible to authenticated users only.
        """
        current_user = get_jwt_identity()

        try:
            reviews = facade.get_all_reviews()
            reviews_data = [{
                "review_id": review.id,
                "text": review.text,
                "rating": review.rating,
                "user_id": review.user_id,
                "place_id": review.place_id,
            } for review in reviews]

            return {"reviews": reviews_data}, 200
        except Exception as e:
            traceback.print_exc()
            raise BadRequest(str(e))

# --------------------- Get Review by ID ---------------------

@api.route('/<review_id>')
class ReviewByID(Resource):
    @jwt_required()
    def get(self, review_id):
        """
        Get a review by its ID.
        Accessible to authenticated users only.
        """
        current_user = get_jwt_identity()

        try:
            review = facade.get_review(review_id)
            if not review:
                raise NotFound("Review not found")

            return {
                "review_id": review.id,
                "text": review.text,
                "rating": review.rating,
                "user_id": review.user_id,
                "place_id": review.place_id,
            }, 200
        except Exception as e:
            traceback.print_exc()
            raise BadRequest(str(e))

# --------------------- Modify a Review ---------------------

@api.route('/<review_id>')
class ReviewModify(Resource):
    @jwt_required()
    @api.expect(review_update_model, validate=True)
    def put(self, review_id):
        """
        Modify a review.
        Administrators can modify all reviews.
        Users can only modify their own reviews.
        """
        current_user = get_jwt_identity()
        review_data = request.json

        review = facade.get_review(review_id)
        if not review:
            raise NotFound("Review not found")

        is_admin = current_user.get('is_admin')
        if not is_admin and review.user_id != current_user.get('id'):
            raise Forbidden("Unauthorized action")

        updated_review = facade.update_review(review_id, review_data)
        return {
            "message": "Review updated successfully",
            "review_id": updated_review.id,
            "text": updated_review.text,
            "rating": updated_review.rating,
        }, 200

    @jwt_required()
    def delete(self, review_id):
        """
        Delete a review.
        Administrators can delete all reviews.
        Users can only delete their own reviews.
        """
        current_user = get_jwt_identity()

        # Retrieve the review
        review = facade.get_review(review_id)
        if not review:
            raise NotFound("Review not found")

        # Check permissions (admin or owner)
        is_admin = current_user.get('is_admin', False)
        if not is_admin and review.user_id != current_user.get('id'):
            raise Forbidden("Unauthorized action")

        # Delete the review
        facade.delete_review(review_id)
        return {"message": "Review deleted successfully"}, 200
