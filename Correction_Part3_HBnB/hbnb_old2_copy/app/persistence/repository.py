# hbnb/app/persistence/repository.py

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from app.models.base_entity import BaseEntity
from app import db


class BaseRepository:
    """
    Base repository providing generic CRUD operations for database entities.
    """
    def __init__(self, entity_class: BaseEntity):
        """
        Initialize the repository with the specified entity class.

        :param entity_class: The SQLAlchemy model class associated with this repository.
        """
        self.entity_class = entity_class
        self.session = scoped_session(sessionmaker(bind=db.engine))

    def get_all(self):
        """
        Retrieve all records for the entity.

        :return: List of all entities.
        """
        try:
            return self.session.query(self.entity_class).all()
        except SQLAlchemyError as e:
            print(f"Error retrieving all {self.entity_class.__name__}: {str(e)}")
            return []

    def get_by_id(self, entity_id: str):
        """
        Retrieve a single entity by its ID.

        :param entity_id: ID of the entity.
        :return: The entity object if found, else None.
        """
        try:
            return self.session.query(self.entity_class).get(entity_id)
        except SQLAlchemyError as e:
            print(f"Error retrieving {self.entity_class.__name__} by ID: {str(e)}")
            return None

    def add(self, entity):
        """
        Add a new entity to the database.

        :param entity: The entity object to add.
        :return: True if successful, False otherwise.
        """
        try:
            self.session.add(entity)
            self.session.commit()
            return True
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error adding {self.entity_class.__name__}: {str(e)}")
            return False

    def update(self, entity):
        """
        Update an existing entity in the database.

        :param entity: The entity object to update.
        :return: True if successful, False otherwise.
        """
        try:
            self.session.merge(entity)
            self.session.commit()
            return True
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error updating {self.entity_class.__name__}: {str(e)}")
            return False

    def delete(self, entity_id: str):
        """
        Delete an entity from the database by its ID.

        :param entity_id: ID of the entity to delete.
        :return: True if successful, False otherwise.
        """
        try:
            entity = self.get_by_id(entity_id)
            if entity:
                self.session.delete(entity)
                self.session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error deleting {self.entity_class.__name__}: {str(e)}")
            return False
