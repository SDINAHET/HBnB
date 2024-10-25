#!/usr/bin/python3
"""
This module defines the HBnBFacade class, which acts as a service layer for
handling operations related to users, places, amenities, and reviews.

It provides methods for creating, retrieving, updating, and managing these
entities by interacting with the underlying repository layer.
"""
from marshmallow import ValidationError
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
from app.persistence.repository import InMemoryRepository


class HBnBFacade:
    """
    The HBnBFacade class provides a unified interface for various services,
    including user management, place management, amenity management, and
    review management. It interacts with the repository layer for persistence.
    """

    def __init__(self):
        """Initialize the HBnBFacade with repositories for users, places,
        reviews, and amenities."""
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # User_service_facade
    def create_user(self, user_data):
        """
        Create a new user and add it to the repository.

        Args:
            user_data (dict): A dictionary containing user details (e.g., first name, last name, email).

        Returns:
            User: The newly created user object.
        """
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """
        Retrieve a user by their ID.

        Args:
            user_id (str): The unique ID of the user.

        Returns:
            User: The user object, or None if the user is not found.
        """
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """
        Retrieve a user by their email.

        Args:
            email (str): The email of the user.

        Returns:
            User: The user object, or None if the user is not found.
        """
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        """
        Retrieve all users from the repository.

        Returns:
            list: A list of all user objects.
        """
        return self.user_repo.get_all()

    def validate_user_data(user_data):
        """Validate the incoming user data."""
        if 'first_name' in user_data and not isinstance(user_data['first_name'], str):
            raise ValidationError("First name must be a string.")
        if 'last_name' in user_data and not isinstance(user_data['last_name'], str):
            raise ValidationError("Last name must be a string.")
        if 'email' in user_data and not self.is_valid_email(user_data['email']):
            raise ValidationError("Invalid email format.")

    def update_user(self, user_id, user_data):
        """
        Update the details of an existing user.

        Args:
            user_id (str): The unique ID of the user to update.
            user_data (dict): A dictionary containing the updated user details.

        Returns:
            User: The updated user object, or None if the user is not found.
        """
        user = self.user_repo.get(user_id)
        if user:
            for key, value in user_data.items():
                setattr(user, key, value)
            self.user_repo.update(user_id, user_data)  # Pass user_id and user_data
            return user
        return None

    # Amenity_service_facade
    def create_amenity(self, amenity_data):
        """
        Create a new amenity and add it to the repository.

        Args:
            amenity_data (dict): A dictionary containing amenity details (e.g., name).

        Returns:
            Amenity: The newly created amenity object.
        """
        new_amenity = Amenity(**amenity_data)
        self.amenity_repo.add(new_amenity)
        return new_amenity

    def get_amenity(self, amenity_id):
        """
        Retrieve an amenity by its ID.

        Args:
            amenity_id (str): The unique ID of the amenity.

        Returns:
            Amenity: The amenity object, or None if not found.
        """
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        """
        Retrieve all amenities from the repository.

        Returns:
            list: A list of all amenity objects.
        """
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        """
        Update the details of an existing amenity.

        Args:
            amenity_id (str): The unique ID of the amenity to update.
            amenity_data (dict): A dictionary containing the updated amenity details.

        Returns:
            Amenity: The updated amenity object, or None if not found.
        """
        amenity = self.amenity_repo.get(amenity_id)
        if amenity:
            for key, value in amenity_data.items():
                setattr(amenity, key, value)
            self.user_repo.update(amenity_id, amenity_data)  # Pass amenity_id and amenity_data
            return amenity
        return None

    # Place_service_facade
    def create_place(self, place_data):
        """
        Create a new place and add it to the repository.

        Args:
            place_data (dict): A dictionary containing place details (e.g., name, description, owner_id).

        Returns:
            Place: The newly created place object.
        """
        new_place = Place(**place_data)
        self.place_repo.add(new_place)
        return new_place

    def get_place(self, place_id):
        """
        Retrieve a place by its ID.

        Args:
            place_id (str): The unique ID of the place.

        Returns:
            Place: The place object, or None if not found.
        """
        place = self.place_repo.get(place_id)
        if place:
            owner = self.user_repo.get(place.owner_id)
            place.owner = owner
            place.amenities = [self.amenity_repo.get(a_id) for a_id in place.amenities]
        return place

    def get_all_places(self):
        """
        Retrieve all places from the repository.

        Returns:
            list: A list of all place objects.
        """
        places = self.place_repo.get_all()
        for place in places:
            place.owner = self.user_repo.get(place.owner_id)
            place.amenities = [self.amenity_repo.get(a_id) for a_id in place.amenities]
        return places

    def update_place(self, place_id, place_data):
        """
        Update the details of an existing place.

        Args:
            place_id (str): The unique ID of the place to update.
            place_data (dict): A dictionary containing the updated place details.

        Returns:
            Place: The updated place object, or None if not found.
        """
        place = self.place_repo.get(place_id)
        if place:
            for key, value in place_data.items():
                if value is not None:
                    setattr(place, key, value)
            self.place_repo.update(place_id, place_data)
            return place
        return None

    # Review_service_facade
    def create_review(self, review_data):
        """
        Create a new review and add it to the repository.

        Args:
            review_data (dict): A dictionary containing review details (e.g., place_id, user_id, text).

        Returns:
            Review: The newly created review object.
        """
        new_review = Review(**review_data)
        self.review_repo.add(new_review)
        return new_review

    def get_review(self, review_id):
        """
        Retrieve a review by its ID.

        Args:
            review_id (str): The unique ID of the review.

        Returns:
            Review: The review object, or None if not found.
        """
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        """
        Retrieve all reviews from the repository.

        Returns:
            list: A list of all review objects.
        """
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        """
        Retrieve all reviews for a specific place.

        Args:
            place_id (str): The unique ID of the place.

        Returns:
            list: A list of review objects for the specified place.
        """
        return self.review_repo.get_by_attribute('place_id', place_id)

    def update_review(self, review_id, review_data):
        """
        Update the details of an existing review.

        Args:
            review_id (str): The unique ID of the review to update.
            review_data (dict): A dictionary containing the updated review details.

        Returns:
            Review: The updated review object, or None if not found.
        """
        review = self.review_repo.get(review_id)
        if review:
            for key, value in review_data.items():
                setattr(review, key, value)
            self.review_repo.update(review_id, review_data) # Pass user_id and user_data
            return review
        return None

    def delete_review(self, review_id):
        """
        Delete a review by its ID.

        Args:
            review_id (str): The unique ID of the review to delete.

        Returns:
            bool: True if the review was deleted, False otherwise.
        """
        review = self.review_repo.get(review_id)
        if review:
            self.review_repo.delete(review_id)
            return True
        return False
