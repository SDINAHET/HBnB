#!/usr/bin/python3

# app/models/base_entity.py
import uuid
from datetime import datetime

class BaseEntity:

    def some_method(self):
        from app.models.review import Review  # Import déplacé ici
        from app.models.base_entity import BaseEntity
        from app.models.place import Place
        from app.models.amenity import Amenity  # Import déplacé ici

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        # self.created_at = datetime.utcnow()  # Use UTC time
        # self.updated_at = datetime.now()
        self.updated_at = self.created_at # Explicitement égal à created_at à l'initialisation
        # self.updated_at = datetime.utcnow()  # Use UTC time

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()
        # self.updated_at = datetime.utcnow()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        # for key, value in data.items():
        #     if hasattr(self, key):
        #         setattr(self, key, value)
        #     else:
        #         print(f"Warning: {key} is not a valid attribute.")

        # self.save()  # Update the updated_at timestamp
        for key, value in data.items():
            if hasattr(self, key):
                try:
                    setattr(self, key, value)
                except Exception as e:
                    print(f"Error setting attribute {key}: {e}")
            else:
                print(f"Warning: {key} is not a valid attribute.")
        self.save()  # Update the updated_at timestamp
