#!/usr/bin/python3

from .base_entity import BaseEntity
from marshmallow import ValidationError


class Amenity(BaseEntity):
    def __init__(self, name: str, description: str = ''):
        super().__init__()
        self.name = name
        # self.description = description
        self.validate()

    def validate(self):
        """Validate the attributes of the amenity."""
        # if not isinstance(self.name, str) or not self.name:
        #     raise ValidationError("Name must be a non-empty string.")
        if len(self.name) > 50:
            raise ValidationError("Name must not exceed 50 characters.")
        # if not isinstance(self.description, str):
        #     raise ValidationError("Description must be a string.")

    def update(self, name: str = None, description: str = None):
        """Update the amenity's attributes."""
        if name is not None:
            self.name = name  # Update name
        # if description is not None:
        #     self.description = description  # Update description
        self.validate()  # Validate the updated values

    def to_dict(self):
        """Return a dictionary representation of the Amenity instance."""
        return {
            'id': self.id,  # Assuming BaseEntity provides an 'id' attribute
            'name': self.name,
            # 'description': self.description,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
