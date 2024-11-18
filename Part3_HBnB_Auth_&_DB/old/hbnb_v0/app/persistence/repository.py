#!/usr/bin/python3

#app/persistence/repository.py
from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        """Add an object to the repository."""
        pass

    @abstractmethod
    def get(self, obj_id):
        """Retrieve an object by its ID."""
        pass

    @abstractmethod
    def get_all(self):
        """Retrieve all objects from the repository."""
        pass

    @abstractmethod
    def update(self, obj_id, data):
        """Update an object with the given ID."""
        pass

    @abstractmethod
    def delete(self, obj_id):
        """Delete an object by its ID."""
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        """Retrieve an object by a specific attribute."""
        pass


class InMemoryRepository(Repository):
    def __init__(self):
        self._storage = {}

    def add(self, obj):
        """Add an object to the repository."""
        self._storage[obj.id] = obj

    def get(self, obj_id):
        """Retrieve an object by ID."""
        return self._storage.get(obj_id)

    def get_all(self):
        """Retrieve all objects in the repository."""
        return list(self._storage.values())

    def update(self, obj_id, data):
        """Update an object in the repository."""
        obj = self.get(obj_id)
        if obj:
            obj.update(data)

    def delete(self, obj_id):
        """Delete an object from the repository."""
        if obj_id in self._storage:
            del self._storage[obj_id]

    def get_by_attribute(self, attr_name, attr_value):
        """Retrieve an object by a specific attribute."""
        return next((obj for obj in self._storage.values() if getattr(obj, attr_name) == attr_value), None)
        # return next(obj for obj in self._storage.values() if getattr(obj, attr_name) == attr_value)
        # return [obj for obj in self._storage.values() if getattr(obj, attr_name) == attr_value]
