# Initialization for persistence layer
# app/persistence/__init__.py

from .repository import Repository, InMemoryRepository

__all__ = ['Repository', 'InMemoryRepository']
