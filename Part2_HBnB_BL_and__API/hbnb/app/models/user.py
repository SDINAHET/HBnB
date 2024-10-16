#!/usr/bin/python3

# app/models/user.py
from .base_entity import BaseEntity
import re
import importlib.util


class User(BaseEntity):

    def __init__(self, firstName, lastName, email, password, isAdmin):
        super().__init__() #appelle le constructeur de BaseEntity
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.isAdmin = isAdmin
