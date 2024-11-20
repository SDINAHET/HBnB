#!/usr/bin/python3
"""
API Endpoints for Reviews.
- Administrators have access to all functionalities (PUT, DELETE without restrictions).
- Users can only modify or delete their own reviews.
"""

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
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

review_update_model = api.model('ReviewUpdate', {
    'content': fields.String(description="New content of the review"),
    'rating': fields.Integer(description="New rating for the review (1 to 5)")
})

# --------------------- Create a Review ---------------------

@api.route('/')
class ReviewList(Resource):
<<<<<<< HEAD
=======
    """
    Resource class for handling review creation and retrieval of all reviews.

    Methods:
        post: Registers a new review.
        get: Retrieves a list of all reviews.
    """

    @api.doc(description='Register a new review', security='BearerAuth')
    # @api.doc(params={'review': 'The review details'})
>>>>>>> 5f57229083636f648161e846b9da23cb00b89a45
    @jwt_required()
    @api.expect(review_model, validate=True)
    def post(self):
        """
        Create a new review.
        Accessible to authenticated users only.
        """
        current_user = get_jwt_identity()
        review_data = request.json

        try:
            review_data['user_id'] = current_user.get('id')
            new_review = facade.create_review(review_data)
            return {
                "message": "Review created successfully",
                "review_id": new_review.id,
                "content": new_review.content,
                "rating": new_review.rating,
                "place_id": new_review.place_id,
            }, 201
        except Exception as e:
            raise BadRequest(str(e))

# --------------------- Get All Reviews ---------------------

<<<<<<< HEAD
@api.route('/')
class ReviewListAll(Resource):
    @jwt_required()
=======
        #ari code


    @api.doc(description='Retrieve a list of all reviews')
    # @api.doc(params={'place_id': 'The ID of the place to retrieve reviews for'})
    @api.response(200, 'List of reviews retrieved successfully')
>>>>>>> 5f57229083636f648161e846b9da23cb00b89a45
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
                "content": review.content,
                "rating": review.rating,
                "user_id": review.user_id,
                "place_id": review.place_id,
            } for review in reviews]
            
            return {"reviews": reviews_data}, 200
        except Exception as e:
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
                "content": review.content,
                "rating": review.rating,
                "user_id": review.user_id,
                "place_id": review.place_id,
            }, 200
        except Exception as e:
            raise BadRequest(str(e))

# --------------------- Modify a Review ---------------------

<<<<<<< HEAD
@api.route('/<review_id>')
class ReviewModify(Resource):
    @jwt_required()
    @api.expect(review_update_model, validate=True)
=======
        return review.to_dict(), 200

    @api.doc(description='Update review details by ID', security='BearerAuth')
    @api.doc(params={'review_id': 'The ID of the review to update'})
    @jwt_required() # add SD
    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    @api.response(401, 'Missing Authorization Header')
    @api.response(403, 'Unauthorized action')
>>>>>>> 5f57229083636f648161e846b9da23cb00b89a45
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
            "content": updated_review.content,
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
