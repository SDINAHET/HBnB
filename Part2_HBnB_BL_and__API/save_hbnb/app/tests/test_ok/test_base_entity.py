import unittest
import time
from datetime import datetime
from app.models.base_entity import BaseEntity

class TestBaseEntity(unittest.TestCase):

    def test_initialization(self):
        """Test if BaseEntity is initialized with correct values."""
        entity = BaseEntity()

        # Vérifiez que l'id est un UUID
        self.assertIsInstance(entity.id, str)
        self.assertEqual(len(entity.id), 36)

        # Vérifiez que created_at et updated_at sont des instances de datetime
        self.assertIsInstance(entity.created_at, datetime)
        self.assertIsInstance(entity.updated_at, datetime)

        # Vérifiez que created_at et updated_at sont identiques à l'initialisation
        self.assertEqual(entity.created_at, entity.updated_at)

    def test_update_after_45_seconds(self):
        """Test that updated_at changes after 45 seconds, but created_at does not."""
        entity = BaseEntity()

        # Vérifiez que created_at et updated_at sont égaux initialement
        self.assertEqual(entity.created_at, entity.updated_at)

        # Attendez 45 secondes
        time.sleep(45)

        # Effectuez une mise à jour de l'objet
        entity.update({'some_attribute': 'new_value'})  # Modifie updated_at, pas created_at

        # Vérifiez que created_at n'a pas changé
        self.assertEqual(entity.created_at, entity.created_at)

        # Vérifiez que updated_at a changé
        self.assertNotEqual(entity.created_at, entity.updated_at)

        # Vérifiez que updated_at est maintenant supérieur à created_at
        self.assertGreater(entity.updated_at, entity.created_at)
