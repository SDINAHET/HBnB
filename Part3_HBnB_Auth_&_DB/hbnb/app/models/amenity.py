# Amenity model definition
from datetime import datetime
from app.models.base_entity import BaseEntity

class Amenity(BaseEntity):
    """
    Amenity class that represents an amenity offered by a place.

    Attributes:
    -----------
    - id (str): Unique identifier for each amenity, inherited from BaseEntity.
    - name (str): The name of the amenity (e.g., "Wi-Fi", "Parking").
    """
    def __init__(self, name):
        super().__init__()
        self.name = name

    def to_dict(self):
        """
        Converts the object attributes to a dictionary representation for easy JSON serialization.

        Returns:
        --------
        dict: A dictionary containing the key-value pairs of the amenity's attributes.
        """
        base_dict = super().to_dict()
        base_dict.update({'name': self.name})
        return base_dict
