# hbnb/app/services/facade.py

"""
HBnBFacade: Central service layer for handling business logic and interacting with repositories.
"""

from app.persistence.repository import Repository
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity


class HBnBFacade:
    """Central service layer for business logic."""

    def __init__(self):
        self.user_repo = Repository(User)
        self.place_repo = Repository(Place)
        self.review_repo = Repository(Review)
        self.amenity_repo = Repository(Amenity)

    # User methods
    def get_all_users(self):
        return self.user_repo.get_all()

    def get_user_by_id(self, user_id):
        return self.user_repo.get_by_id(user_id)

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def delete_user(self, user_id):
        return self.user_repo.delete(user_id)

    # Place methods
    def get_all_places(self):
        return self.place_repo.get_all()

    def get_place_by_id(self, place_id):
        return self.place_repo.get_by_id(place_id)

    def create_place(self, place_data):
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def delete_place(self, place_id):
        return self.place_repo.delete(place_id)

    # Review methods
    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_review_by_id(self, review_id):
        return self.review_repo.get_by_id(review_id)

    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def delete_review(self, review_id):
        return self.review_repo.delete(review_id)

    # Amenity methods
    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def get_amenity_by_id(self, amenity_id):
        return self.amenity_repo.get_by_id(amenity_id)

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def update_amenity(self, amenity_id, update_data):
        amenity = self.amenity_repo.get_by_id(amenity_id)
        if not amenity:
            return None
        for key, value in update_data.items():
            if hasattr(amenity, key):
                setattr(amenity, key, value)
        self.amenity_repo.update(amenity)
        return amenity

    def delete_amenity(self, amenity_id):
        return self.amenity_repo.delete(amenity_id)
