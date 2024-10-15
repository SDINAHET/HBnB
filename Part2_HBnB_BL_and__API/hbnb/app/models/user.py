#!/usr/bin/python3

# app/models/user.py
from base_entity import BaseEntity
import re
import importlib.util


class User(BaseEntity):

    def __init__(self, firstName, lastName, email, password, isAdmin):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.isAdmin = isAdmin

    def registerProfile(self):
        pass

    def updateProfile(self):
        pass

    # def deleteProfile(self):
    #     pass
