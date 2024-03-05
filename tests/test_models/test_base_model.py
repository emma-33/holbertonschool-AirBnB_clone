#!/usr/bin/python3
"""Unittest for base model class"""

import unittest
import uuid
from datetime import datetime, timedelta
from models.base_model import BaseModel


class TestBaseModelInit(unittest.TestCase):
    """test for base model class"""
    def test_no_kwargs(self):
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_with_kwargs(self):
        my_model = BaseModel(name="My First Model", value=89)
        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.value, 89)

    def test_created_at_updated_at_kwargs(self):
        my_model = BaseModel(created_at=datetime.now(),
                             updated_at=datetime.now())
        self.assertLessEqual(abs(datetime.now() - my_model.created_at),
                             timedelta(seconds=1))
        self.assertLessEqual(abs(datetime.now() - my_model.updated_at),
                             timedelta(seconds=1))

    def test_ignore_class_key(self):
        my_model = BaseModel(__class__="My Class")
        self.assertNotIn("__class__", my_model.__dict__)


if __name__ == '__main__':
    unittest.main()
