
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, data):
        user = User(**data)
        self.user_repo.add(user)
        return user

    def create_place(self, data):
        place = Place(**data)
        self.place_repo.add(place)
        return place

    def create_review(self, data):
        review = Review(**data)
        self.review_repo.add(review)
        return review

    def create_amenity(self, data):
        amenity = Amenity(**data)
        self.amenity_repo.add(amenity)
        return amenity
    