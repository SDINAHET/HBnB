#!/usr/bin/python3
"""
This module defines the HBnBFacade class, which acts as a service layer for
handling operations related to users, places, amenities, and reviews.

It provides methods for creating, retrieving, updating, and managing these
entities by interacting with the underlying repository layer.
"""
import logging

from marshmallow import ValidationError
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
from app.persistence.sqlalchemy_repository import SQLAlchemyRepository

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
        self.user_repository = SQLAlchemyRepository(User)  # Switched to SQLAlchemyRepository
        self.place_repository = SQLAlchemyRepository(Place)
        self.review_repository = SQLAlchemyRepository(Review)
        self.amenity_repository = SQLAlchemyRepository(Amenity)

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
        # amenity = self.amenity_repo.get(amenity_id)
        # if amenity:
        #     for key, value in amenity_data.items():
        #         setattr(amenity, key, value)
        #     # self.user_repo.update(amenity_id, amenity_data)  # Pass amenity_id and amenity_data
        #     # amenity.update(**amenity_data)
        #     self.amenity_repo.update(amenity_id, amenity_data)
        #     return amenity
        # return None

        try:
            # Obtenir l'amenity par ID
            amenity = self.amenity_repo.get(amenity_id)
            if not amenity:
                raise ValueError("Amenity not found")

            # Appliquer les modifications
            for key, value in amenity_data.items():
                setattr(amenity, key, value)

            # Sauvegarder les modifications dans la base de données
            self.amenity_repo.update(amenity_id, amenity_data)
            return amenity
        except Exception as e:
            logging.error(f"Error in update_amenity: {e}")
            raise

    # Place_service_facade
    def create_place(self, place_data):
        """
        Create a new place and add it to the repository.

        Args:
            place_data (dict): A dictionary containing place details (e.g., name, description, owner_id).

        Returns:
            Place: The newly created place object.
        """
        owner_id = place_data['owner_id']
        owner = self.user_repo.get(place_data['owner_id'])
        if not owner:
            raise ValueError("Owner not found")

        # Récupérer et initialiser les amenities
        amenities = []
        if 'amenities' in place_data:
            amenities = [self.amenity_repo.get(amenity_id) for amenity_id in place_data['amenities']]
            # Filtrer les amenities valides
            amenities = [amenity for amenity in amenities if amenity is not None]

        # Créer une nouvelle instance de Place
        place = Place(
            title=place_data['title'],
            description=place_data.get('description'),
            price=place_data['price'],
            latitude=place_data['latitude'],
            longitude=place_data['longitude'],
            owner_id=place_data['owner_id'],  # Ensure this is included
            owner=owner,   # Associate owner instance
            # amenities=place_data.get['amenities'],
            # amenities=place_data.get('amenities', []),
            # reviews=[],  # ou data.get('reviews', []) # **
            # amenities=[]  # ou data.get('amenities', [])
            amenities=amenities
            )

        # # Ajouter les amenities si présentes
        # if 'amenities' in place_data:
        #     amenities = [self.amenity_repo.get(amenity_id) for amenity_id in place_data['amenities']]
        #     new_place.amenities = [amenity for amenity in amenities if amenity is not None]

        try:
            # Ajouter la nouvelle place au repository
            self.place_repo.add(place)
        # owner = self.user_repo.get(place_data['owner_id'])
            logging.info(f"Successfully created place: {place}")

        # # Ajoutez la place au dictionnaire
        # places_data[place_id] = new_place
        except Exception as e:
            logging.error(f"Error adding place: {e}")
            raise ValueError(f"Error adding place: {str(e)}")
            # Log the error or handle it as appropriate
            # print(f"Error creating place: {e}")
            # return None
        return place

    def get_place(self, place_id):
        """
        Retrieve a place by its ID.

        Args:
            place_id (str): The unique ID of the place.

        Returns:
            Place: The place object, or None if not found.
        """
        logger.info(f"Retrieving place with ID: {place_id}")
        place = self.place_repo.get(place_id)

        if place:
            logger.info(f"Found place: {place}")

            # Récupérer le propriétaire de la place
            owner = self.user_repo.get(place.owner_id)
            place.owner = owner
            logger.info(f"Associated owner: {owner}")

            # Récupérer les amenities basées sur les IDs
            if place.amenities:  # Vérifiez si la place a des IDs d'amenities
                amenities = [self.amenity_repo.get(a_id) for a_id in place.amenities]
                # Filtrer pour enlever les None
                place.amenities = [amenity for amenity in amenities if amenity is not None]
                logger.info(f"Associated amenities: {place.amenities}")

        else:
            logger.warning(f"No place found with ID: {place_id}")

        return place
        # return self.place_repo.get(place_id)

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
        logger.info(f"Updating place with ID: {place_id}")
        # place = self.place_repo.get(place_id)

        # if place:
        #     for key, value in place_data.items():
        #         if value is not None:
        #             setattr(place, key, value)
        #     self.place_repo.update(place_id, place_data)
        #     return place
        # logger.warning(f"No place found with ID: {place_id} to update.")
        # return None
        logger.info(f"Updating place with ID: {place_id}")
        try:
            # Obtenir le place par ID
            place = self.place_repo.get(place_id)
            if not place:
                raise ValueError("Place not found")

            # Appliquer les modifications
            for key, value in place_data.items():
                setattr(place, key, value)

            # Sauvegarder les modifications dans la base de données
            self.place_repo.update(place_id, place_data)
            return place
        except Exception as e:
            logging.error(f"Error in update_place: {e}")
            raise

    def check_owner_exists(self, owner_id):
        # Implémentez la logique pour vérifier si l'owner existe
        owner = get_owner_by_id(owner_id)  # Récupérez l'owner par ID
        return owner is not None

    def check_amenity_exists(self, amenity_id):
        # Implémentez la logique pour vérifier si l'amenity existe
        amenity = get_amenity_by_id(amenity_id)  # Récupérez l'amenity par ID
        return amenity is not None

    def user_has_reviewed_place(self, user_id, place_id):
        reviews = self.review_repo.get_by_attribute('user_id', user_id)
        if reviews is None:
            return False
        for review in reviews:
            if review.place_id == place_id:
                return True
        return False

    # Review_service_facade
    # def create_review(self, review_data):
    # # def create_review(self, text, rating, user_id, place_id):
    #     """
    #     Create a new review and add it to the repository.

    #     Args:
    #         review_data (dict): A dictionary containing review details (e.g., place_id, user_id, text).

    #     Returns:
    #         Review: The newly created review object.
    #     """
    #     # new_review = Review(review_data)
    #     # self.review_repo.add(new_review)
    #     # return new_review

    #     # try:
    #     #     review = Review(
    #     #         text=review_data['text'],
    #     #         rating=review_data['rating'],
    #     #         user_id=review_data['user_id'],
    #     #         place_id=review_data['place_id']
    #     #     )
    #     #     self.review_repo.add(review)
    #     #     return review
    #     # except Exception as e:
    #     #     logging.error(f"Error in create_review: {e}")
    #     #     raise

    #     # #code ari
    #     # user_id = review_data.get('user_id')
    #     # place_id = review_data.get('place_id')

    #     # place = self.get_place(place_id)
    #     # if not place:
    #     #     raise ValueError("Place not found")

    #     # if str(place.owner_id) == str(user_id):
    #     #     raise ValueError("Cannot review your own place")

    #     # existing_reviews = self.review_repo.get_by_attribute('user_id', user_id)
    #     # for review in existing_reviews:
    #     #     if review.place_id == place_id:
    #     #         raise ValueError("Already reviewed this place")

    #     # review = Review(**review_data)
    #     # review.validate()
    #     # self.review_repo.add(review)
    #     # return review

    #     # Validation des données d'entrée


    #     # Validation des données d'entrée
    #     required_fields = ['user_id', 'place_id', 'text', 'rating']
    #     for field in required_fields:
    #         if field not in review_data:
    #             raise ValueError(f"Missing required field: {field}")

    #     user_id = review_data.get('user_id')
    #     place_id = review_data.get('place_id')

    #     # Vérifiez si le lieu existe
    #     place = self.get_place(place_id)
    #     if not place:
    #         raise ValueError("Place not found")

    #     # Vérifiez si l'utilisateur est le propriétaire du lieu
    #     if str(place.owner_id) == str(user_id):
    #         raise ValueError("Cannot review your own place")

    #     # Vérifiez si l'utilisateur a déjà critiqué ce lieu
    #     existing_reviews = self.review_repo.get_by_attribute('user_id', user_id) or []
    #     for review in existing_reviews:
    #         if review.place_id == place_id:
    #             raise ValueError("Already reviewed this place")

    #     # Création de la critique
    #     try:
    #         user = User.get_by_id(user_id)
    #         if not user:
    #             raise ValueError("User not found")
    #         review = Review(text=review_data['text'], rating=review_data['rating'], user=user, place=place)
    #         review.validate()  # Validation de la critique
    #         self.review_repo.add(review)
    #         return review
    #     except Exception as e:
    #         logging.error(f"Error in create_review: {e}")
    #         raise ValueError("An error occurred while creating the review")


    # def get_review(self, review_id):
    #     """
    #     Retrieve a review by its ID.

    #     Args:
    #         review_id (str): The unique ID of the review.

    #     Returns:
    #         Review: The review object, or None if not found.
    #     """
    #     return self.review_repo.get(review_id)

    # def get_all_reviews(self):
    #     """
    #     Retrieve all reviews from the repository.

    #     Returns:
    #         list: A list of all review objects.
    #     """
    #     return self.review_repo.get_all()

    # def get_reviews_by_place(self, place_id):
    #     """
    #     Retrieve all reviews for a specific place.

    #     Args:
    #         place_id (str): The unique ID of the place.

    #     Returns:
    #         list: A list of review objects for the specified place.
    #     """
    #     return self.review_repo.get_by_attribute('place_id', place_id)

    # def update_review(self, review_id, review_data):
    #     """
    #     Update the details of an existing review.

    #     Args:
    #         review_id (str): The unique ID of the review to update.
    #         review_data (dict): A dictionary containing the updated review details.

    #     Returns:
    #         Review: The updated review object, or None if not found.
    #     """
    #     review = self.review_repo.get(review_id)
    #     if review:
    #         for key, value in review_data.items():
    #             setattr(review, key, value)
    #         self.review_repo.update(review_id, review_data) # Pass user_id and user_data
    #         return review
    #     return None

    # def delete_review(self, review_id):
    #     """
    #     Delete a review by its ID.

    #     Args:
    #         review_id (str): The unique ID of the review to delete.

    #     Returns:
    #         bool: True if the review was deleted, False otherwise.
    #     """
    #     review = self.review_repo.get(review_id)
    #     if review:
    #         self.review_repo.delete(review_id)
    #         return True
    #     return False

    def create_review(self, review_data):
        required_fields = ['user_id', 'place_id', 'text', 'rating']
        for field in required_fields:
            if field not in review_data:
                raise ValueError(f"Missing required field: {field}")

        user_id = review_data['user_id']
        place_id = review_data['place_id']

        # Verify if the place exists
        place = Place.get_by_id(place_id)
        if not place:
            raise ValueError("Place not found")

        # Verify if the user exists
        user = User.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")

        # Verify if the user is the owner of the place
        if str(place.owner_id) == str(user_id):
            raise ValueError("Cannot review your own place")

        # Verify if the user has already reviewed the place
        existing_reviews = self.review_repo.get_by_attribute('user_id', user_id) or []
        for review in existing_reviews:
            if review.place_id == place_id:
                raise ValueError("Already reviewed this place")

        # Create the review
        try:
            review = Review(
                comment=review_data['text'],
                rating=review_data['rating'],
                user=user,
                place=place
            )
            self.review_repo.add(review)  # Add the review to the repository
            return review

        except Exception as e:
            logging.error(f"Error in create_review: {e}")
            raise ValueError("An error occurred while creating the review")

    def get_review(self, review_id):
        """Retrieve a review by its ID."""
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        """Retrieve all reviews from the repository."""
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        """Retrieve all reviews for a specific place."""
        return self.review_repo.get_by_attribute('place_id', place_id)

    def update_review(self, review_id, review_data):
        """Update the details of an existing review."""
        review = self.review_repo.get(review_id)
        if review:
            for key, value in review_data.items():
                setattr(review, key, value)
            self.review_repo.update(review_id, review_data)
            return review
        return None

    def delete_review(self, review_id):
        """Delete a review by its ID."""
        review = self.review_repo.get(review_id)
        if review:
            self.review_repo.delete(review_id)
            return True
        return False
