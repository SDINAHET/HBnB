from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from app.persistence.repository import BaseRepository
from app import db
from werkzeug.security import generate_password_hash

class HBnBFacade:
    """
    A facade for handling business logic and interactions between models and repositories.
    """

    def __init__(self):
        self.user_repo = BaseRepository(User)
        self.place_repo = BaseRepository(Place)
        self.review_repo = BaseRepository(Review)
        self.amenity_repo = BaseRepository(Amenity)

    # User operations
    def create_user(self, first_name, last_name, email, password, is_admin=False):
        """
        Create a new user with hashed password.
        """
        if self.user_repo.filter_by(email=email):
            return {"error": "Email already exists."}, 409

        hashed_password = generate_password_hash(password)
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=hashed_password,
            is_admin=is_admin,
        )
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """
        Retrieve a user by their ID.
        """
        return self.user_repo.get_by_id(user_id)

    def get_all_users(self):
        """
        Retrieve all users.
        """
        return self.user_repo.get_all()

    def update_user(self, user_id, updates):
        """
        Update user details, excluding password and email.
        """
        if "password" in updates or "email" in updates:
            return {"error": "Cannot update email or password via this endpoint."}, 400

        return self.user_repo.update(user_id, updates)

    def delete_user(self, user_id):
        """
        Delete a user by ID.
        """
        return self.user_repo.delete(user_id)

    # Place operations
    def create_place(self, title, description, price, latitude, longitude, owner_id):
        """
        Create a new place.
        """
        owner = self.user_repo.get_by_id(owner_id)
        if not owner:
            return {"error": "Owner does not exist."}, 404

        if not (-90.0 <= latitude <= 90.0):
            return {"error": "Latitude must be between -90 and 90."}, 400

        if not (-180.0 <= longitude <= 180.0):
            return {"error": "Longitude must be between -180 and 180."}, 400

        place = Place(
            title=title,
            description=description,
            price=price,
            latitude=latitude,
            longitude=longitude,
            owner=owner,
        )
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        """
        Retrieve a place by its ID.
        """
        return self.place_repo.get_by_id(place_id)

    def get_all_places(self):
        """
        Retrieve all places.
        """
        return self.place_repo.get_all()

    def update_place(self, place_id, updates):
        """
        Update a place's details.
        """
        return self.place_repo.update(place_id, updates)

    def delete_place(self, place_id):
        """
        Delete a place by ID.
        """
        return self.place_repo.delete(place_id)

    # Review operations
    def create_review(self, text, rating, user_id, place_id):
        """
        Create a new review.
        """
        user = self.user_repo.get_by_id(user_id)
        place = self.place_repo.get_by_id(place_id)
        if not user:
            return {"error": "User does not exist."}, 404
        if not place:
            return {"error": "Place does not exist."}, 404

        if not (1 <= rating <= 5):
            return {"error": "Rating must be between 1 and 5."}, 400

        if self.review_repo.first_by(user_id=user_id, place_id=place_id):
            return {"error": "User has already reviewed this place."}, 409

        review = Review(
            text=text,
            rating=rating,
            user=user,
            place=place,
        )
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        """
        Retrieve a review by its ID.
        """
        return self.review_repo.get_by_id(review_id)

    def get_all_reviews(self):
        """
        Retrieve all reviews.
        """
        return self.review_repo.get_all()

    def update_review(self, review_id, updates):
        """
        Update a review's details.
        """
        return self.review_repo.update(review_id, updates)

    def delete_review(self, review_id):
        """
        Delete a review by ID.
        """
        return self.review_repo.delete(review_id)

    # Amenity operations
    def create_amenity(self, name):
        """
        Create a new amenity.
        """
        if self.amenity_repo.first_by(name=name):
            return {"error": "Amenity with this name already exists."}, 409

        amenity = Amenity(name=name)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        """
        Retrieve an amenity by its ID.
        """
        return self.amenity_repo.get_by_id(amenity_id)

    def get_all_amenities(self):
        """
        Retrieve all amenities.
        """
        return self.amenity_repo.get_all()

    def delete_amenity(self, amenity_id):
        """
        Delete an amenity by ID.
        """
        return self.amenity_repo.delete(amenity_id)
