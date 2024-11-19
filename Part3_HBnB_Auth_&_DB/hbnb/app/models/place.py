# Place model definition
from app.models.base_entity import BaseEntity

class Place(BaseEntity):
    """
    Place class representing a place in the HBnB application.

    Attributes:
    -----------
    - title (str): Title of the place.
    - description (str): Detailed description of the place.
    - price (float): Price per night for the place.
    - latitude (float): Latitude coordinate for the place location.
    - longitude (float): Longitude coordinate for the place location.
    - owner_id (str): ID of the user who owns the place.
    """
    def __init__(self, title, price, latitude, longitude, owner_id, description=None):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id

    def to_dict(self):
        """
        Converts the object attributes to a dictionary representation for easy JSON serialization.

        Returns:
        --------
        dict: A dictionary containing the key-value pairs of the place's attributes.
        """
        place_dict = super().to_dict()
        place_dict.update({
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner_id
        })
        return place_dict
