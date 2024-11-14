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
"""
import logging
from marshmallow import fields, ValidationError
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
    Resource class for handling review creation and retrieval of all reviews.

    Methods:
        post: Registers a new review.
        get: Retrieves a list of all reviews.
    """

    @api.doc(description='Register a new review')
    # @api.doc(params={'review': 'The review details'})
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """
        Register a new review.
        ----------------------

        Parameters:
        -----------
        `self`: The instance of the Resource class.

        Returns:
        --------
        tuple: A tuple containing:
            - dict: Newly created review details.
                - `text` (str): Text of the review.
                - `rating` (int): Rating of the place (1-5).
                - `user_id` (str): ID of the user who created the review.
                - `place_id` (str): ID of the place being reviewed.
            - int: HTTP status code (201) for successful creation.

        Raises:
        -------
        400: If the input data is invalid.
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

    @api.doc(description='Retrieve a list of all reviews')
    # @api.doc(params={'place_id': 'The ID of the place to retrieve reviews for'})
    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """
        Retrieve a list of all reviews.
        -------------------------------

        Parameters:
        -----------
        `self`: The instance of the Resource class.

        Returns:
        --------
        tuple: A tuple containing:
            - List[dict]: List of all reviews.
                - `text` (str): Text of the review.
                - `rating` (int): Rating of the place (1-5).
                - `user_id` (str): ID of the user who created the review.
                - `place_id` (str): ID of the place being reviewed.
            - int: HTTP status code (200) for successful retrieval.

        Raises:
        -------
        """

        reviews = facade.get_all_reviews()
        return [review.to_dict() for review in reviews], 200


@api.route('/<review_id>')
class ReviewResource(Resource):
    """
    Resource class for handling single review operations.

    Methods:
        get: Retrieves review details by review ID.
        put: Updates review details by review ID.
        delete: Deletes review by review ID.
    """

    @api.doc(description='Retrieve review details by ID')
    @api.doc(params={'review_id': 'The ID of the review to retrieve'})
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """
        Get review details by ID.
        -------------------------

        Parameters:
        ----------
        `self`: The instance of the Resource class.
        `review_id` (str): The ID of the review to retrieve.

        Returns:
        --------
        tuple: A tuple containing:
            - dict: Review details.
                -text (str): Text of the review.
                -rating (int): Rating of the place (1-5).
                -user_id (str): ID of the user who created the review.
                -place_id (str): ID of the place being reviewed.
            - int: HTTP status code (200) for successful retrieval.

        Raises:
        -------
        404: If the review is not found.
        """

        review = facade.get_review_by_id(review_id)
        if review is None:
            api.abort(404, 'Review not found')

        return review.to_dict(), 200

    @api.doc(description='Update review details by ID')
    @api.doc(params={'review_id': 'The ID of the review to update'})
    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):
        """
        Update a review's information.
        ------------------------------

        Parameters:
        ----------
        `self`: The instance of the Resource class.
        `review_id` (str): The ID of the review to update.

        Returns:
        ---------
        tuple: A tuple containing:
            - dict: Updated review details
                - `text` (str): Text of the review
                - `rating` (int): Rating of the place (1-5)
                - `user_id` (str): ID of the user.
                - `place_id` (str): ID of the place.
            - int: HTTP status code (200) for successful update.

        Raises:
        --------
        404: If the review is not found.
        400: If the input data is invalid.
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

    @api.doc(description='Delete a review by ID')
    @api.doc(params={'review_id': 'The ID of the review to delete'})
    @api.response(204, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """
        Delete a review.
        ----------------

        Parameters:
        ----------
        `self`: The instance of the Resource class.
        `review_id` (str): The ID of the review to delete.

        Returns:
        --------
        tuple: A tuple containing:
            - `str`: Empty string indicating success.
            - int: HTTP status code (204) for successful deletion.

        Raises:
        -------
        404: If the review is not found.
        """

        review = facade.get_review_by_id(review_id)
        if review is None:
            api.abort(404, 'Review not found')

        facade.delete_review(review_id)
        return '', 204

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    """
    Resource class for handling retrieval of reviews for a specific place.

    Methods:
        get: Retrieves all reviews associated with a specific place by place ID.
    """

    @api.doc(description='Retrieve all reviews for a specific place')
    @api.doc(params={'place_id': 'The ID of the place to retrieve reviews for'})
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """
        Get all reviews for a specific place.
        -------------------------------------

        Parameters:
        ----------
        `self`: The instance of the Resource class.
        `place_id` (str): The ID of the place to retrieve reviews for.

        Returns:
        --------
        tuple: A tuple containing:
            - List[dict]: List of reviews for the specified place.
                - `text` (str): Text of the review.
                - `rating` (int): Rating of the place (1-5).
                - `user_id` (str): ID of the user who created the review.
                - `place_id` (str): ID of the place being reviewed
            - int: HTTP status code (200) for successful retrieval.

        Raises:
        -------
        404: If the place is not found or has no reviews.
        """

        reviews = facade.get_reviews_by_place_id(place_id)
        if not reviews:
            api.abort(404, 'Place not found or no reviews for this place')

        return [review.to_dict() for review in reviews], 200
