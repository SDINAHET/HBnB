# Review endpoints code
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Content of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'place_id': fields.String(required=True, description='ID of the place being reviewed')
})

@api.route('/')
class ReviewList(Resource):
    @jwt_required()
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    @api.response(401, 'Unauthorized')
    def post(self):
        """
        Create a new review for a place.
        ------------------------------

        Parameters:
        -----------
        - `self`: Reference to the instance of the resource class.

        Expects:
        --------
        - JSON payload matching the `review_model`, with fields such as:
            - `text` (str): Content of the review.
            - `rating` (int): Rating of the place (1-5).
            - `place_id` (str): ID of the place being reviewed.

        Returns:
        --------
        - (dict): JSON response with the details of the created review.
        - Status code 201 if successful.
        - Status code 400 if input data is invalid.
        - Status code 401 if user is not authorized.
        """
        data = api.payload
        current_user = get_jwt_identity()

        # Logic to ensure the user doesn't own the place they are reviewing
        place = facade.get_place(data['place_id'])
        if not place:
            return {'error': 'Place not found'}, 404

        if place.owner_id == current_user['id']:
            return {'error': 'You cannot review your own place'}, 400

        # Check if the user has already reviewed the place
        existing_review = facade.get_review_by_user_and_place(current_user['id'], data['place_id'])
        if existing_review:
            return {'error': 'You have already reviewed this place'}, 400

        # Create a new review using the facade
        new_review = facade.create_review(current_user['id'], data)
        return new_review, 201

@api.route('/<review_id>')
class ReviewResource(Resource):
    @jwt_required()
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """
        Get a review's details by ID.
        -----------------------------

        Parameters:
        -----------
        - `review_id` (str): ID of the review to retrieve.

        Returns:
        --------
        - (dict): JSON response with the details of the review.
        - Status code 200 if successful.
        - Status code 404 if the review is not found.
        """
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        return review, 200

    @jwt_required()
    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Unauthorized action')
    def put(self, review_id):
        """
        Update a review's information.
        ------------------------------

        Parameters:
        -----------
        - `review_id` (str): ID of the review to update.

        Expects:
        --------
        - JSON payload matching the `review_model`, with updated fields.

        Returns:
        --------
        - (dict): JSON response indicating successful update.
        - Status code 200 if successful.
        - Status code 400 if input data is invalid.
        - Status code 403 if user is not authorized to modify the review.
        - Status code 404 if the review is not found.
        """
        data = api.payload
        current_user = get_jwt_identity()

        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404

        # Check if the review belongs to the current user
        if review.user_id != current_user['id']:
            return {'error': 'Unauthorized action'}, 403

        # Update the review
        updated_review = facade.update_review(review_id, data)
        return updated_review, 200

    @jwt_required()
    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    @api.response(403, 'Unauthorized action')
    def delete(self, review_id):
        """
        Delete a review by ID.
        ----------------------

        Parameters:
        -----------
        - `review_id` (str): ID of the review to delete.

        Returns:
        --------
        - (dict): JSON response indicating successful deletion.
        - Status code 200 if successful.
        - Status code 403 if user is not authorized to delete the review.
        - Status code 404 if the review is not found.
        """
        current_user = get_jwt_identity()

        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404

        # Check if the review belongs to the current user
        if review.user_id != current_user['id']:
            return {'error': 'Unauthorized action'}, 403

        # Delete the review using the facade
        facade.delete_review(review_id)
        return {'message': 'Review deleted successfully'}, 200
