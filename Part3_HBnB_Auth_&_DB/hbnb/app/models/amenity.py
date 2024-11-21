#!/usr/bin/python3

from .base_entity import BaseEntity
from marshmallow import ValidationError
from app.extension import db
from datetime import datetime


class Amenity(BaseEntity):
    __tablename__ = 'amenities'
    
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)  # 50 caractères max pour le nom
    description = db.Column(db.String(255), default="")  # Optionnel, maximum 255 caractères
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Date de création
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)  # Date de mise à jour

    places = db.relationship('Place', secondary='place_amenities', back_populates='amenities', lazy='subquery')

    def __init__(self, name: str, description: str = None):
        super().__init__()
        self.name = name
        self.description = description
        self.validate()

    def validate(self):
        """Validate the attributes of the amenity."""
        if len(self.name) > 50:
            raise ValidationError("Name must not exceed 50 characters.")
        if len(self.description) > 255:
            raise ValidationError("Description must not exceed 255 characters.")

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

place_amenities = db.Table('place_amenities',
    db.Column('place_id', db.Integer, db.ForeignKey('places.id'), primary_key=True),
    db.Column('amenity_id', db.Integer, db.ForeignKey('amenities.id'), primary_key=True)
)
