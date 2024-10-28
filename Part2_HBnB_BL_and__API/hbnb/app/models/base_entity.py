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

# app/models/base_entity.py
import uuid
from datetime import datetime

class BaseEntity:
    """Classe de base pour les entités avec gestion d'identifiant et de timestamps.

    Attributs :
        id (str) : Identifiant unique de l'entité, généré lors de l'initialisation.
        created_at (datetime) : Timestamp indiquant quand l'entité a été créée.
        updated_at (datetime) : Timestamp indiquant la dernière mise à jour de l'entité.
    """

    def __init__(self):
        """Initialise une instance de BaseEntity.

        Génère un identifiant unique et initialise les timestamps de création
        et de mise à jour.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at # Explicitement égal à created_at à l'initialisation

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                try:
                    setattr(self, key, value)
                except Exception as e:
                    print(f"Error setting attribute {key}: {e}")
            else:
                print(f"Warning: {key} is not a valid attribute.")
        self.save()  # Update the updated_at timestamp

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

    def some_method(self):
        # Import seulement si nécessaire pour éviter les importations circulaires
        from app.models.review import Review
        from app.models.place import Place
        from app.models.amenity import Amenity
        from app.models.review import Review

    # def some_method(self):
    #     from app.models.base_entity import ValidationError
    #     from app.models.review import Review  # Import déplacé ici
    #     # from app.models.base_entity import BaseEntity
    #     from app.models.place import Place
    #     from app.models.amenity import Amenity  # Import déplacé ici
