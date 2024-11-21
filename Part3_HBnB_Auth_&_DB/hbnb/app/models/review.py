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

    def __init__(self, comment: str, rating: int, user: User, place: Place):
        """Initialise une instance de Review.

        Args :
            comment (str) : Commentaire de l'évaluation.
            rating (int) : Note de l'évaluation (entre 1 et 5).
            user (User) : Instance de l'utilisateur ayant laissé l'évaluation.
            place (Place) : Instance du lieu évalué.

        Lève une ValueError si les attributs ne sont pas valides.
        """
        super().__init__()
        self.comment = comment
        self.rating = rating
        self.user_id = user.id
        self.place_id = place.id
        self.validate()
        self.register_review(user, place)

    def validate(self):
        if not isinstance(self.comment, str) or not self.comment:
            raise ValueError('Comment must be a non-empty string.')
        if not isinstance(self.rating, int) or self.rating < 1 or self.rating > 5:
            raise ValueError('Rating must be an integer between 1 and 5.')
        user = User.query.get(self.user_id)
        place = Place.query.get(self.place_id)
        if not user:
            raise ValueError("User does not exist.")
        if not place:
            raise ValueError("Place does not exist.")


    def register_review(self, user: User, place: Place):
        """Link the review to the user and place."""
        user.add_review(self)
        place.add_review(self)

    @staticmethod
    def get_by_id(review_id: str) -> 'Review':
        return Review.repository.get(review_id)

    def get_user(self):
        return User.get_by_id(self.user_id)

    def get_place(self):
        return Place.get_by_id(self.place_id)

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
