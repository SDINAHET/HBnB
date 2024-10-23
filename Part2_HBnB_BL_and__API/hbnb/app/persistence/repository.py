#!/usr/bin/python3

#app/persistence/repository.py
from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass


class InMemoryRepository(Repository):
    def __init__(self):
        self._storage = {}

    def add(self, obj):
        self._storage[obj.id] = obj

    def get(self, obj_id):
        return self._storage.get(obj_id)

    def get_all(self):
        return list(self._storage.values())

    def update(self, obj_id, data):
        # obj = self.get(obj_id)
        # if obj:
        #     obj.update(data
        #                )

        # obj = self.get(obj_id)
        # if obj:
        #     # Assuming 'data' is a dictionary with the attributes to update
        #     for key, value in data.items():
        #         if hasattr(obj, key):
        #             setattr(obj, key, value)
        # Retrieve the object by its ID
        obj = self.get(obj_id)
        if obj is None:
            logging.warning(f"Update failed: Object with ID {obj_id} not found.")
            return False  # Indicate that the object was not found

        try:
            # Update the object's attributes with the new data
            obj.update(data)  # Ensure the object's update method handles the data correctly

            # Optionally save the updated object back to the storage (if applicable)
            self.save(obj)  # Implement the save logic if needed

            logging.info(f"Object with ID {obj_id} updated successfully.")
            return True  # Indicate that the update was successful

        except Exception as e:
            logging.error(f"Error updating object {obj_id}: {e}")  # Log the error
            return False  # Indicate that the update failed

    def delete(self, obj_id):
        if obj_id in self._storage:
            del self._storage[obj_id]

    def get_by_attribute(self, attr_name, attr_value):
        return next((obj for obj in self._storage.values() if getattr(obj, attr_name) == attr_value), None)

    # def update(self, amenity_id, amenity):
    #     """
    #     Update the details of an existing amenity in the repository.

    #     Args:
    #         amenity_id (str): The unique ID of the amenity to update.
    #         amenity (Amenity): The updated amenity object.

    #     Returns:
    #         None
    #     """
    #     # Find the existing amenity by ID and replace it with the updated one
    #     if amenity_id in self.data:
    #         self.data[amenity_id] = amenity  # Assuming `data` is a dict-like storage
