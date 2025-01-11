#!/usr/bin/python3
"""
This module defines the HBnBFacade class, which acts as a service layer for
handling operations related to users, places, amenities, and reviews.

It provides methods for creating, retrieving, updating, and managing these
entities by interacting with the underlying repository layer.
"""
import logging

from app.extension import db, bcrypt
from marshmallow import ValidationError
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
from app.persistence.sqlalchemy_repository import UserRepository, PlaceRepository, ReviewRepository, AmenityRepository
from app.persistence.sqlalchemy_repository import SQLAlchemyRepository
from werkzeug.exceptions import BadRequest, Forbidden, NotFound
import re
from flask import current_app
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from uuid import UUID



class UserCreationError(Exception):
    """Custom exception raised when user creation fails."""
    pass

# Configure logging
logging.basicConfig(level=logging.INFO)  # You can adjust the level as needed
logger = logging.getLogger(__name__)  # Create a logger for this module

class HBnBFacade:
    """
    The HBnBFacade class provides a unified interface for various services,
    including user management, place management, amenity management, and
    review management. It interacts with the repository layer for persistence.
    """

    def __init__(self):
        """Initialize the HBnBFacade with repositories for users, places,
        reviews, and amenities."""
        self.user_repo = UserRepository() # Switched to SQLAlchemyRepository
        self.place_repository = PlaceRepository()
        self.review_repository = ReviewRepository()
        self.amenity_repository = AmenityRepository()

    def is_valid_email(self, email):
        """
        Validates the email format.
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    # User_service_facade
    def create_user(self, user_data):
        try:
            self.validate_user_data(user_data)

            # Ensure password is hashed
            if 'password' in user_data:
                user_data['password'] = bcrypt.generate_password_hash(user_data['password']).decode('utf-8')
                current_app.logger.info(f"Hashed password for {user_data['email']}: {user_data['password']}")  # Log hashed password
            
            user = User(**user_data)
            db.session.add(user)
            db.session.commit()
            return user

        except KeyError as e:
            current_app.logger.error(f"Missing required field: {e}")
            raise ValueError(f"Missing required field: {e}")
        except IntegrityError as e:
            current_app.logger.error(f"Integrity error: {str(e)}")
            db.session.rollback()  # Rollback any changes on error
            raise UserCreationError("Database integrity error. Please check the user data.")
        except Exception as e:
            current_app.logger.error(f"Unexpected error: {str(e)}")
            raise UserCreationError(f"Error creating user: {str(e)}")

    def get_user(self, user_id):
        """
        Retrieve a user by their ID.
        """
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """
        Retrieve a user by their email..
        """
        return User.query.filter_by(email=email).first()
    
    def get_all_users(self):
        """
        Retrieve all users from the repository.
        """
        return self.user_repo.get_all()

    def validate_user_data(self, user_data):
        if 'first_name' in user_data and not isinstance(user_data['first_name'], str):
            raise ValidationError("First name must be a string.")
        if 'last_name' in user_data and not isinstance(user_data['last_name'], str):
            raise ValidationError("Last name must be a string.")
        if 'email' in user_data and not self.is_valid_email(user_data['email']):
            raise ValidationError("Invalid email format.")

    def update_user(self, user_id, user_data):
        """
        Update the details of an existing user.
        """
        user = self.user_repo.get(user_id)
        if user:
            for key, value in user_data.items():
                setattr(user, key, value)
            self.user_repo.update(user_id, user_data)  # Pass user_id and user_data
            return user
        return None

    # Amenity_service_facade
    def create_amenity(self, data):
        """
        Create a new amenity and add it to the repository.
        """
        if not data.get('name'):
            raise BadRequest("Amenity name is required.")
        
        existing_amenity = self.amenity_repository.get_by_name(data['name'])
        if existing_amenity:
            raise BadRequest(f"Amenity with name '{data['name']}' already exists.")
        
        new_amenity = Amenity(name=data['name'], description=data.get('description', ''))
        self.amenity_repository.add(new_amenity)
        return new_amenity

    def get_amenity(self, amenity_id):
        """
        Retrieve an amenity by its ID.
        """
        amenity = self.amenity_repository.get(amenity_id)
        if not amenity:
            raise NotFound(f"Amenity with ID {amenity_id} not found.")
        return amenity

    def get_all_amenities(self):
        """
        Retrieve all amenities from the repository.
        """
        return self.amenity_repository.get_all()

    def update_amenity(self, amenity_id, data):
        """
        Update the details of an existing amenity.
        """
        updated_amenity = self.amenity_repository.update(amenity_id, data)
        if not updated_amenity:
            raise NotFound(f"Amenity with ID {amenity_id} not found.")
        return updated_amenity

    def delete_amenity(self, amenity_id):
        """Delete amenity by id"""
        result = self.amenity_repository.delete(amenity_id)
        if not result:
            raise NotFound(f"Amenity with ID {amenity_id} not found.")
        return {"message": "Amenity deleted successfully."}

    @staticmethod
    def create_place(title, description, price, latitude, longitude, owner_id, amenities):
        """
        Crée un nouveau lieu et l'ajoute à la base de données.
        """
        if not title or not description or not price or not latitude or not longitude or not owner_id:
            raise ValueError("Missing required data to create place")
    
        # Fetch the owner from the database
        owner = User.query.get(owner_id)
        if not owner:
            raise ValueError("Owner not found")

        # Create the new Place object, with the owner as an actual object, not just an ID
        place = Place(
            title=title,
            description=description,
            price=price,
            latitude=latitude,
            longitude=longitude,
            owner_id=str(owner_id)  # Here, we pass the actual User object, not just the owner_id
        )

        # Save the place to the database
        place.save()

        # Link amenities to the place
        for amenity_id in amenities:
            # Fetch the amenity from the database
            amenity = Amenity.query.get(amenity_id)
            if amenity:
                place.amenities.append(amenity)

        # Save the updated place with amenities
        place.save()

        return place

    @staticmethod
    def get_place_by_id(place_id):
        """
        Retrieves a single place by its ID from the database.
        """
        try:
            return Place.query.get(place_id)
        except NoResultFound:
            return None

    @staticmethod
    def list_places():
        """
        Retrieves all places from the database.
        """
        return Place.query.all()

    def update_place(self, place_id, data):
        """
        Updates the place with the given ID using the provided data.
        """
        place = Place.query.get(place_id)
        if not place:
            raise ValueError("Place not found")

        # Update place fields with the provided data
        if 'title' in data:
            place.title = data['title']
        if 'description' in data:
            place.description = data['description']
        if 'price' in data:
            place.price = data['price']
        if 'latitude' in data:
            place.latitude = data['latitude']
        if 'longitude' in data:
            place.longitude = data['longitude']

        # Handle amenities update
        if 'amenities' in data:
            # Remove existing amenities
            place.amenities.clear()
            for amenity_id in data['amenities']:
                amenity = Amenity.query.get(amenity_id)
                if amenity:
                    place.amenities.append(amenity)

        # Save the updated place
        place.save()

        return place

    def delete_place(self, place_id):
        """
        Deletes the place with the given ID from the database.
        """
        place = Place.query.get(place_id)
        if place:
            place.delete()
        else:
            raise ValueError("Place not found")

    def user_has_reviewed_place(self, user_id, place_id):
        reviews = self.review_repository.get_by_attribute('user_id', user_id)
        if reviews is None:
            return False
        for review in reviews:
            if review.place_id == place_id:
                return True
        return False

    def create_review(self, review_data):
        """Create a new review."""
        try:
            user_id = UUID(review_data['user_id'])
            place_id = UUID(review_data['place_id'])
        except ValueError:
            raise ValueError("Invalid UUID format for user_id or place_id")

        # Retrieve the User and Place instances using the UUIDs
        user = User.query.filter_by(id=user_id).first()
        place = Place.query.filter_by(id=place_id).first()
        
        if not user or not place:
            raise ValueError("Invalid user_id or place_id")

        # Create the Review instance with the User and Place instances
        review = Review(
            comment=review_data['comment'],
            rating=review_data['rating'],
            user=user,  # Pass the User instance
            place=place  # Pass the Place instance
        )

        # Add the review to the repository
        self.review_repository.add(review)
        return review

    def get_review(self, review_id):
        """Retrieve a review by its ID."""
        return self.review_repository.get(review_id)

    def get_all_reviews(self):
        """Retrieve all reviews from the repository."""
        return self.review_repository.get_all()

    def get_reviews_by_place(self, place_id):
        """Retrieve all reviews for a specific place."""
        return self.review_repository.get_by_attribute('place_id', place_id)

    def update_review(self, review_id, review_data):
        """Update the details of an existing review."""
        return self.review_repository.update(review_id, review_data)

    def delete_review(self, review_id):
        """Delete a review by its ID."""
        return self.review_repository.delete(review_id)
