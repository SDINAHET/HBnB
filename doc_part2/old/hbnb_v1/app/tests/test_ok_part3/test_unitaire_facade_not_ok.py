import unittest
# from app.services.facade import HBnBFacade
# from app.models.place import Place
# from app.models.user import User
# from app.models.amenity import Amenity
# from app.persistence.repository import InMemoryRepository

class TestHBnBFacade(unittest.TestCase):
    def setUp(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.facade = HBnBFacade(self.user_repo, self.place_repo, self.review_repo, self.amenity_repo)

        self.user = User(id="user_id", first_name="Test", last_name="User", email="testuser@example.com")
        self.user_repo.add(self.user)

        self.amenity1 = Amenity(id="amenity1_id", name="WiFi")
        self.amenity2 = Amenity(id="amenity2_id", name="Pool")
        self.amenity_repo.add(self.amenity1)
        self.amenity_repo.add(self.amenity2)

    def test_create_place(self):
        place_data = {
            "title": "Test Place",
            "description": "A nice place",
            "price": 100.0,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": "user_id",
            "amenities": ["amenity1_id", "amenity2_id"]
        }
        place = self.facade.create_place(place_data)
        self.assertEqual(place.title, "Test Place")
        self.assertEqual(place.owner_id, "user_id")
        self.assertEqual(len(place.amenities), 2)

    def test_get_place(self):
        place_data = {
            "title": "Test Place",
            "description": "A nice place",
            "price": 100.0,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": "user_id",
            "amenities": ["amenity1_id", "amenity2_id"]
        }
        place = self.facade.create_place(place_data)
        retrieved_place = self.facade.get_place(place.id)
        self.assertEqual(retrieved_place.title, "Test Place")

    def test_update_place(self):
        place_data = {
            "title": "Test Place",
            "description": "A nice place",
            "price": 100.0,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": "user_id",
            "amenities": ["amenity1_id", "amenity2_id"]
        }
        place = self.facade.create_place(place_data)
        update_data = {
            "title": "Updated Place",
            "description": "An updated nice place",
            "price": 150.0
        }
        updated_place = self.facade.update_place(place.id, update_data)
        self.assertEqual(updated_place.title, "Updated Place")
        self.assertEqual(updated_place.price, 150.0)

if __name__ == '__main__':
    unittest.main()
