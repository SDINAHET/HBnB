
from .base_entity import BaseEntity

class Place(BaseEntity):
    def __init__(self, title, price, latitude, longitude, owner_id):
        super().__init__()
        self.title = title
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.amenities = []
    