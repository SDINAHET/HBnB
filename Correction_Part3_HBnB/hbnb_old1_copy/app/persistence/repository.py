from app import db
from sqlalchemy.exc import SQLAlchemyError

class BaseRepository:
    """
    A generic repository class for handling common CRUD operations.

    Attributes:
        model (db.Model): The SQLAlchemy model class for the repository.
    """

    def __init__(self, model):
        """
        Initialize the repository with the specified SQLAlchemy model.

        Args:
            model (db.Model): The SQLAlchemy model class to manage.
        """
        self.model = model

    def add(self, entity):
        """
        Add a new entity to the database.

        Args:
            entity (db.Model): The entity instance to add.

        Returns:
            The added entity.

        Raises:
            SQLAlchemyError: If a database error occurs.
        """
        try:
            db.session.add(entity)
            db.session.commit()
            return entity
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    def get_by_id(self, entity_id):
        """
        Retrieve an entity by its primary key.

        Args:
            entity_id: The ID of the entity to retrieve.

        Returns:
            The entity instance, or None if not found.
        """
        return self.model.query.get(entity_id)

    def get_all(self):
        """
        Retrieve all entities of the model.

        Returns:
            List of all entities of the model.
        """
        return self.model.query.all()

    def update(self, entity_id, updates):
        """
        Update an entity with the specified data.

        Args:
            entity_id: The ID of the entity to update.
            updates (dict): A dictionary of field-value pairs to update.

        Returns:
            The updated entity, or None if not found.

        Raises:
            SQLAlchemyError: If a database error occurs.
        """
        entity = self.get_by_id(entity_id)
        if not entity:
            return None
        try:
            for key, value in updates.items():
                if hasattr(entity, key):
                    setattr(entity, key, value)
            db.session.commit()
            return entity
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    def delete(self, entity_id):
        """
        Delete an entity by its primary key.

        Args:
            entity_id: The ID of the entity to delete.

        Returns:
            True if deletion was successful, False if entity not found.

        Raises:
            SQLAlchemyError: If a database error occurs.
        """
        entity = self.get_by_id(entity_id)
        if not entity:
            return False
        try:
            db.session.delete(entity)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    def filter_by(self, **kwargs):
        """
        Retrieve entities filtered by the given criteria.

        Args:
            **kwargs: Field-value pairs to filter by.

        Returns:
            List of entities matching the criteria.
        """
        return self.model.query.filter_by(**kwargs).all()

    def first_by(self, **kwargs):
        """
        Retrieve the first entity matching the given criteria.

        Args:
            **kwargs: Field-value pairs to filter by.

        Returns:
            The first entity matching the criteria, or None if no match.
        """
        return self.model.query.filter_by(**kwargs).first()
