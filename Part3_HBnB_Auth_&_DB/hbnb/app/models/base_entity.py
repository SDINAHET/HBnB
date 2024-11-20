#!/usr/bin/python3

"""
Module : base_entity

Ce module définit la classe BaseEntity, qui sert de classe de base pour
d'autres entités dans l'application. La classe fournit des attributs
communs tels qu'un identifiant unique, des timestamps de création et de
mise à jour, ainsi que des méthodes pour sauvegarder et mettre à jour
les attributs de l'objet.

Classes :
    BaseEntity : Classe de base pour les entités, fournissant des attributs
                 communs et des méthodes de gestion.
    ValidationError : Exception personnalisée pour les erreurs de validation.
"""

from app.extension import db
import uuid
from datetime import datetime

class BaseEntity(db.Model):
    __abstract__ = True

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, **kwargs):
        """Initializes a BaseModel instance with attributes, 
        generating id and setting timestamps on creation."""
        super().__init__(**kwargs)
        if not self.id:
            self.id = str(uuid.uuid4())  # Generate UUID if not provided
        if not self.created_at:
            self.created_at = datetime.utcnow()  # Default created_at to current time
        if not self.updated_at:
            self.updated_at = self.created_at  # Set updated_at to created_at initially
            
    def save(self):
        """Updates the updated_at timestamp whenever the object is modified."""
        self.updated_at = datetime.utcnow()
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        """Updates the attributes of the object based on the provided dictionary."""
        for key, value in data.items():
            if hasattr(self, key):
                try:
                    setattr(self, key, value)
                except Exception as e:
                    print(f"Error setting attribute {key}: {e}")
            else:
                print(f"Warning: {key} is not a valid attribute.")
        self.save()  # Update the updated_at timestamp and save

    def delete(self):
        """Deletes the current object from the database."""
        db.session.delete(self)
        db.session.commit()


class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass
