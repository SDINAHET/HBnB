#!/usr/bin/python3

from .base_entity import BaseEntity
from marshmallow import ValidationError
from sqlalchemy import Column, String, Integer

class Amenity(BaseEntity):
    __tablename__ = 'amenities'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)  # 50 caractères max pour le nom
    description = Column(String(255))  # Optionnel, maximum 255 caractères

    def __init__(self, name: str, description: str=''):
        super().__init__()
        self.name = name
        self.description = description
        self.validate()

    def validate(self):
        """Validate the attributes of the amenity."""
        if len(self.name) > 50:
            raise ValidationError("Name must not exceed 50 characters.")

    def update(self, name: str = None, description: str = None):
        """Update the amenity's attributes."""
        if name is not None:
            self.name = name  # Update name
        if description is not None:
            self.description = description  # Update description
        self.validate()  # Validate the updated values

    def to_dict(self):
        """Return a dictionary representation of the Amenity instance."""
        return {
            'id': self.id,  # Assuming BaseEntity provides an 'id' attribute
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
