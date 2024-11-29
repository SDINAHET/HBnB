# hbnb/app/models/base_entity.py

"""
Define the BaseEntity class for shared attributes and functionality across models.
"""

import uuid
from datetime import datetime
from app.models import db

class BaseEntity(db.Model):
    """
    BaseEntity class
    A base model with common attributes for all entities in the HBnB application.
    """

    __abstract__ = True

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def save(self):
        """
        Save the current instance to the database.
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        Delete the current instance from the database.
        """
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        """
        Convert the base entity to a dictionary representation.
        This method is meant to be overridden by subclasses.
        Returns:
            dict: Dictionary representation of the entity.
        """
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
