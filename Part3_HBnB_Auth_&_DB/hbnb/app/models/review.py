# #!/usr/bin/python3
"""
Module : review

Ce module définit la classe Review, qui représente une évaluation d'un
lieu par un utilisateur. La classe hérite de BaseEntity et fournit
des méthodes pour valider et gérer les évaluations associées à des
utilisateurs et des lieux.

Classes :
    Review : Représente une évaluation d'un lieu par un utilisateur.
"""

from __future__ import annotations  # Doit être la première ligne
from .base_entity import BaseEntity
from app.models.user import User
from app.models.place import Place  # Uncommented to use Place class directly
from typing import TYPE_CHECKING
from app.extension import db
from datetime import datetime

if TYPE_CHECKING:
    from .user import User
    from .place import Place

class Review(BaseEntity):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.String(500), nullable=False)  # Texte de l'avis, limité à 500 caractères
    rating = db.Column(db.Integer, nullable=False)  # Note de l'avis (1-5)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Date de création
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)  # Date de mise à jour
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)  # ID de l'utilisateur
    place_id = db.Column(db.Integer, db.ForeignKey('places.id'), nullable=False)  # ID du lieu

    user = db.relationship('User', back_populates='reviews')  # Relation avec l'utilisateur (User)
    place = db.relationship('Place', back_populates='reviews')  # Relation avec le lieu (Place)

    def __init__(self, comment: str, rating: int, user: User, place: Place):
        """Initialise une instance de Review.
        """
        super().__init__()
        self.comment = comment
        self.rating = rating
        self.user = user
        self.place = place
        self.validate()

    def validate(self):
        if not isinstance(self.comment, str) or not self.comment:
            raise ValueError('Comment must be a non-empty string.')
        if not isinstance(self.rating, int) or self.rating < 1 or self.rating > 5:
            raise ValueError('Rating must be an integer between 1 and 5.')
        if not isinstance(self.user, User):
            raise ValueError('User must be an instance of User.')
        if not isinstance(self.place, Place):
            raise ValueError('Place must be an instance of Place.')

    def to_dict(self):
        """Return a dictionary representation of the Review instance."""
        return {
            'id': self.id,
            'comment': self.comment,
            'rating': self.rating,
            'user': self.get_user().to_dict() if self.get_user() else None,
            'place': self.get_place().to_dict() if self.get_place() else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
