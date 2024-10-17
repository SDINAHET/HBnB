#!/usr/bin/python3

from .base_entity import BaseEntity


class Amenity(BaseEntity):
    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description
