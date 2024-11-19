# Review model definition
from app.models.base_entity import BaseEntity
from app.models.user import User
from app.models.place import Place

class Review(BaseEntity):
    """
    Review model representing reviews made by users for places.

    Attributes:
    -----------
    - text (str): The content of the review, required.
    - rating (int): Rating given to the place, must be between 1 and 5.
    - place (Place): Reference to the Place being reviewed, must exist.
    - user (User): Reference to the User who wrote the review, must exist.
    """
    def __init__(self, text, rating, place: Place, user: User):
        super().__init__()
        self.text = text
        self.rating = self._validate_rating(rating)
        self.place = place
        self.user = user

    def _validate_rating(self, rating):
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5.")
        return rating

    def to_dict(self):
        """
        Converts the object attributes to a dictionary representation for easy JSON serialization.

        Returns:
        --------
        dict: A dictionary containing the key-value pairs of the review's attributes.
        """
        base_dict = super().to_dict()
        base_dict.update({
            'text': self.text,
            'rating': self.rating,
            'place_id': self.place.id,
            'user_id': self.user.id
        })
        return base_dict
