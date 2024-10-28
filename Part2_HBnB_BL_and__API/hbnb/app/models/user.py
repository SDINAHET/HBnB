#!/usr/bin/python3

"""
Module pour la gestion des utilisateurs dans une application de location.

Ce module définit la classe `User`, qui représente un utilisateur dans le système.
La classe hérite de `BaseEntity` et inclut des méthodes pour valider les attributs,
enregistrer les utilisateurs, et gérer les avis et les lieux associés à l'utilisateur.

Classes:
    - User: Représente un utilisateur avec des détails tels que le prénom, le nom, l'email,
      le statut d'administrateur, les lieux possédés et les avis écrits.

Attributs:
    - users (Dict[str, 'User']): Dictionnaire de niveau de classe pour stocker les utilisateurs.

Méthodes:
    - __init__(first_name, last_name, email, is_admin=False): Initialise une instance de `User`.
    - validate_first_name(first_name): Valide que le prénom est entre 1 et 50 caractères.
    - validate_last_name(last_name): Valide que le nom de famille est entre 1 et 50 caractères.
    - validate_email(email): Valide le format de l'email et s'assure qu'il est unique.
    - is_valid_email(email): Vérifie si l'email est au format valide.
    - register_user(): Enregistre l'utilisateur dans le dictionnaire de niveau de classe.
    - get_reviews(): Renvoie la liste des avis écrits par l'utilisateur.
"""

from marshmallow import ValidationError
import re
from typing import List, Dict
from app.models.base_entity import BaseEntity


class User(BaseEntity):

    users: Dict[str, 'User'] = {} # Class-level storage for users

    def __init__(self, first_name, last_name, email, is_admin=False):
        """
        Initialise une instance de `User`.

        Args:
            first_name (str): Prénom de l'utilisateur.
            last_name (str): Nom de famille de l'utilisateur.
            email (str): Adresse e-mail de l'utilisateur.
            is_admin (bool, optional): Indique si l'utilisateur est un administrateur. Par défaut, False.

        Raises:
            ValidationError: Si le prénom, le nom de famille ou l'email ne respectent pas les règles de validation.
        """
        super().__init__() #appelle le constructeur de BaseEntity
        self.first_name = self.validate_first_name(first_name)
        self.last_name = self.validate_last_name(last_name)
        self.email = self.validate_email(email)
        self.is_admin = is_admin  # Ajoutez cet attribut si nécessaire
        self.places: List['Place'] = []  # Places owned by the user
        self.reviews: List['Review'] = []  # Reviews written by the user
        self.register_user()  # ajout

    def validate_first_name(self, first_name):
        """
        Valide que le prénom est un non vide et a une longueur maximale de 50 caractères.

        Args:
            first_name (str): Prénom à valider.

        Returns:
            str: Prénom validé.

        Raises:
            ValidationError: Si le prénom est vide ou dépasse 50 caractères.
        """
        if not first_name or len(first_name) > 50:
            raise ValidationError("First name must be between 1 and 50 characters.")
        return first_name

    def validate_last_name(self, last_name):
        """
        Valide que le nom de famille est un non vide et a une longueur maximale de 50 caractères.

        Args:
            last_name (str): Nom de famille à valider.

        Returns:
            str: Nom de famille validé.

        Raises:
            ValidationError: Si le nom de famille est vide ou dépasse 50 caractères.
        """
        if not last_name or len(last_name) > 50:
            raise ValidationError("Last name must be between 1 and 50 characters.")
        return last_name

    def register_user(self):
        """
        Enregistre l'utilisateur dans le dictionnaire de classe.

        Raises:
            ValidationError: Si un utilisateur avec cet email existe déjà.
        """
        # Vérifie si un utilisateur avec cet email existe déjà
        if any(user.email == self.email for user in User.users.values()):
            raise ValidationError("An account with this email already exists.")
        User.users[self.id] = self

    @staticmethod
    def is_valid_email(email):
        """
        Vérifie si l'email est au format valide.

        Args:
            email (str): Email à valider.

        Returns:
            bool: True si l'email est valide, False sinon.
        Simple regex for email validation
        """
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(regex, email) is not None

    def validate_email(self, email):
        """
        Valide le format de l'email et s'assure qu'il est unique.

        Args:
            email (str): Email à valider.

        Returns:
            str: Email validé.

        Raises:
            ValidationError: Si l'email est invalide ou déjà utilisé.
        """
        if not self.is_valid_email(email):
            raise ValidationError("Invalid email format.")
        return email

    # def add_place(self, place):
    #     """Add a place to the user's list of places."""
    #     self.places.append(place)
    #     self.save()  # Update timestamp when adding a place

    # def add_review(self, review):
    #     """Add a review to the user's list of reviews."""
    #     self.reviews.append(review)
    #     self.save()  # Update timestamp when adding a place

    def get_reviews(self):
        """
        Renvoie la liste des avis écrits par l'utilisateur.

        Returns:
            List[Review]: Liste des avis associés à l'utilisateur.
        """
        return self.reviews
