#!/usr/bin/python3

from .base_entity import BaseEntity
from marshmallow import ValidationError


class Amenity(BaseEntity):
    """
    Amenity entity class, extending BaseEntity with attributes for name and description.

    Attributes:
        name (str): Name of the amenity.
        description (str): Description of the amenity.
    """

    def __init__(self, name: str, description: str = ''):
        """
        Initialize a new Amenity instance with a name and optional description.
        
        Args:
            name (str): Name of the amenity.
            description (str, optional): Description of the amenity. Defaults to ''.
        
        Raises:
            ValidationError: If validation fails for name or description.
        """
        super().__init__()
        self.name = name
        self.description = description
        self.validate()

    def validate(self):
        """
        Validate the attributes of the Amenity instance.

        Raises:
            ValidationError: If name is not a valid non-empty string,
                             or exceeds character length, or if description is not a string.
        """
        if not isinstance(self.name, str) or not self.name:
            raise ValidationError("Name must be a non-empty string.")
        if len(self.name) > 50:
            raise ValidationError("Name must not exceed 50 characters.")
        if not isinstance(self.description, str):
            raise ValidationError("Description must be a string.")

    def update(self, name: str = None, description: str = None):
        """
        Update the Amenity instance's attributes and re-validate.

        Args:
            name (str, optional): New name for the amenity.
            description (str, optional): New description for the amenity.
        
        Raises:
            ValidationError: If updated attributes fail validation.
        """
        if name is not None:
            self.name = name  # Update name
        if description is not None:
            self.description = description  # Update description
        self.validate()  # Validate the updated values

    def to_dict(self):
        """
        Return a dictionary representation of the Amenity instance.

        Returns:
            dict: Dictionary with amenity details, including timestamps.
        """
        return {
            'id': self.id,  # Assuming BaseEntity provides an 'id' attribute
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
