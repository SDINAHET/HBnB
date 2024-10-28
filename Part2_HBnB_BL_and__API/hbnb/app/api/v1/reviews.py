#!/usr/bin/python3
"""
app/api/v1/reviews.py

This module defines the API endpoints for managing reviews in the HBnB application.
It provides functionalities to create, retrieve, update, and delete reviews, as well
as fetching reviews for a specific place.

The API is built using Flask-RESTx, and the module integrates with the business logic layer
through the HBnBFacade, adhering to a Facade pattern to manage interactions with entities.

Endpoints:
    - POST /api/v1/reviews/: Register a new review.
    - GET /api/v1/reviews/: Return a list of all reviews.
    - GET /api/v1/reviews/<review_id>: Retrieve details of a specific review.
    - GET /api/v1/places/<place_id>/reviews: Retrieve all reviews for a specific place.
    - PUT /api/v1/reviews/<review_id>: Update a review’s information.
    - DELETE /api/v1/reviews/<review_id>: Delete a review.

Models:
    - Review: Defines the schema for review data used for input validation and documentation.
    - User: Represents the user who created the review.
    - Place: Represents the place being reviewed.

Error Handling:
    - Returns **201** on successful creation (POST).
    - Returns **200** on successful retrieval and updates (GET, PUT).
    - Returns **204** on successful deletion (DELETE).
    - Returns **400** for invalid input data (POST, PUT).
    - Returns **404** if the requested review or place is not found (GET, DELETE).
"""

from flask_restx import Namespace, Resource, fields
from typing import List
from app.services import facade

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})


@api.route('/')
class ReviewList(Resource):
    """
    Resource to manage a collection of reviews.

    - POST: Creates a new review with the provided data.
    - GET: Retrieves a list of all reviews.
    """

    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """
        Register a new review for a place.

        Expects JSON data matching the `review_model` for validation.

        Returns:
            - 201 status code with the created review's data if successful.
            - 400 status code if input data is invalid.
        """
        data = api.payload
        if not data:
            api.abort(400, 'Invalid input data')

        text = data['text']
        rating = data['rating']
        user_id = data['user_id']
        place_id = data['place_id']

        # Create a new review instance
        new_review = facade.create_review(
            text=text,
            rating=rating,
            user_id=user_id,
            place_id=place_id
        )

        return new_review.to_dict(), 201

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """
        Retrieve a list of all reviews in the system.

        Returns:
            - 200 status code with a list of reviews, each in dictionary format.
        """
        reviews = facade.get_all_reviews()
        return [review.to_dict() for review in reviews], 200


@api.route('/<review_id>')
class ReviewResource(Resource):
    """
    Resource to manage individual reviews based on review_id.

    - GET: Retrieve details of a specific review.
    - PUT: Update a review's information.
    - DELETE: Delete a review.
    """

    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """
        Get details for a specific review by ID.

        Args:
            review_id (str): The ID of the review to retrieve.

        Returns:
            - 200 status code with review data if found.
            - 404 status code if the review is not found.

        Example:
            GET /api/v1/reviews/12345
        """
        review = facade.get_review_by_id(review_id)
        if review is None:
            api.abort(404, 'Review not found')

        return review.to_dict(), 200

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):
        """
        Update a review's information by ID.

        Expects JSON data matching the `review_model` for validation.

        Args:
            review_id (str): The ID of the review to update.

        Returns:
            - 200 status code with the updated review data if successful.
            - 400 status code if input data is invalid.
            - 404 status code if the review is not found.
        """
        review = facade.get_review_by_id(review_id)
        if review is None:
            api.abort(404, 'Review not found')

        data = api.payload
        if not data:
            api.abort(400, 'Invalid input data')

        if 'text' in data:
            review.text = data['text']
        if 'rating' in data:
            review.rating = data['rating']

        updated_review = facade.update_review(review)
        return updated_review.to_dict(), 200

    @api.response(204, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """
        Delete a review by ID.

        Args:
            review_id (str): The ID of the review to delete.

        Returns:
            - 204 status code if deletion is successful.
            - 404 status code if the review is not found.
        """
        review = facade.get_review_by_id(review_id)
        if review is None:
            api.abort(404, 'Review not found')

        facade.delete_review(review_id)
        return '', 204

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    """
    Resource to retrieve reviews associated with a specific place.

    - GET: Retrieve all reviews for a specific place.
    """

    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """
        Retrieve all reviews for a specific place by place ID.

        Args:
            place_id (str): The ID of the place whose reviews to retrieve.

        Returns:
            - 200 status code with a list of reviews if any are found.
            - 404 status code if the place is not found or has no reviews.

        Example:
            GET /api/v1/places/54321/reviews
        """
        reviews = facade.get_reviews_by_place_id(place_id)
        if not reviews:
            api.abort(404, 'Place not found or no reviews for this place')

        return [review.to_dict() for review in reviews], 200
