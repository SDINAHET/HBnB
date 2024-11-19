# Base model class definition
import uuid
from datetime import datetime

class BaseEntity:
    """
    BaseEntity class serves as a base class for other models.

    Attributes:
    -----------
    - id (str): Unique identifier for each entity, generated as a UUID4.
    - created_at (datetime): Timestamp when the entity is created.
    - updated_at (datetime): Timestamp when the entity is last updated.
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        Updates the `updated_at` timestamp to the current time whenever changes are made.
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        Converts the object attributes to a dictionary representation for easy JSON serialization.

        Returns:
        --------
        dict: A dictionary containing the key-value pairs of the entity's attributes.
        """
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
