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
from sqlalchemy.dialects.postgresql import UUID
import uuid

if TYPE_CHECKING:
    from .user import User
    from .place import Place

class Review(BaseEntity):
    __tablename__ = 'reviews'  # Define the table name once

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    comment = db.Column(db.String(500), nullable=False)  # Review comment (max 500 characters)
    rating = db.Column(db.Integer, nullable=False)  # Review rating (1-5)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Creation timestamp
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)  # Update timestamp

    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=False)
    place_id = db.Column(UUID(as_uuid=True), db.ForeignKey('places.id'), nullable=False)

    # Relationships
    user = db.relationship('User', back_populates='reviews', lazy=True)  # Relation with User (one-to-many)
    place = db.relationship('Place', back_populates='reviews', lazy=True)  # Relation with Place (one-to-many)

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
