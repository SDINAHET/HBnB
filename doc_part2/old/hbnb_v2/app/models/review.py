
from .base_entity import BaseEntity

class Review(BaseEntity):
    def __init__(self, text, rating, user_id, place_id):
        super().__init__()
        self.text = text
        self.rating = rating
        self.user_id = user_id
        self.place_id = place_id
    