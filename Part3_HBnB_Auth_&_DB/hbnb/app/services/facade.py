from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity


class HBnBFacade:
    """
    HBnBFacade acts as a bridge between the API and the persistence layer, handling
    the business logic and ensuring the correct interactions between entities.
    """
    def __init__(self):
        self.user_repository = InMemoryRepository()
        self.place_repository = InMemoryRepository()
        self.review_repository = InMemoryRepository()
        self.amenity_repository = InMemoryRepository()

    # User Management
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repository.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repository.get(user_id)

    def update_user(self, user_id, data):
        self.user_repository.update(user_id, data)

    # Place Management
    def create_place(self, place_data):
        place = Place(**place_data)
        self.place_repository.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repository.get(place_id)

    def update_place(self, place_id, data):
        self.place_repository.update(place_id, data)

    def get_all_places(self):
        return self.place_repository.get_all()

    # Review Management
    def create_review(self, review_data):
        review = Review(**review_data)
        place = self.get_place(review.place.id)
        if place.owner.id == review.user.id:
            raise ValueError("You cannot review your own place.")
        if any(r.user.id == review.user.id for r in self.get_reviews_by_place(place.id)):
            raise ValueError("You have already reviewed this place.")
        self.review_repository.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repository.get(review_id)

    def update_review(self, review_id, data):
        self.review_repository.update(review_id, data)

    def delete_review(self, review_id):
        self.review_repository.delete(review_id)

    def get_reviews_by_place(self, place_id):
        return [review for review in self.review_repository.get_all() if review.place.id == place_id]

    # Amenity Management
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repository.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repository.get(amenity_id)

    def update_amenity(self, amenity_id, data):
        self.amenity_repository.update(amenity_id, data)

    def get_all_amenities(self):
        return self.amenity_repository.get_all()
