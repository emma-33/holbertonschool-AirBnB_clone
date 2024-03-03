#!/usr/bin/python3
""" Module for test Base_model class """
from models.base_model import BaseModel
import unittest
from datetime import datetime, timedelta

""" class test DefineBaseModel """


class TestDefineBaseModel(unittest.TestCase):

    def test_instantiation(self):
        """ test new instance of Base model """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_attribute_name(self):
        """ test new instance with name """
        my_model = BaseModel()
        my_model.name = "My First Model"
        self.assertEqual(my_model.name, "My First Model")

    def test_attribute_number(self):
        """ test new instance with number """
        my_model = BaseModel()
        my_model.number = 70
        self.assertEqual(my_model.number, 70)

    def test_date_creation(self):
        """ test date new instance """
        my_model = BaseModel()
        current_time = datetime.now()
        self.assertLessEqual
        (my_model.created_at, current_time + timedelta(seconds=1))

    def test_date_update(self):
        """ test date update instance """
        my_model = BaseModel()
        current_time = datetime.now()
        self.assertEqual
        (my_model.updated_at, current_time + timedelta(seconds=1))

    def test_id(self):
        """ test creation id """
        model1 = BaseModel()
        model2 = BaseModel()

        self.assertTrue(isinstance(model1.id, str))
        self.assertTrue(isinstance(model2.id, str))
        self.assertTrue(len(model1.id) > 0)
        self.assertTrue(len(model2.id) > 0)

        self.assertNotEqual(model1.id, model2.id)


class TestStrBaseModel(unittest.TestCase):
    def test_str(self):
        """ test representation to a string """
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.number = 5

        str_representation = str(my_model)

        expected_str = "[BaseModel] ({}) {}".format
        (my_model.id, my_model.__dict__)


class TestSaveBaseModel(unittest.TestCase):
    def test_save(self):
        """ test updates the public instance attribute
        updated_at with the current datetime """
        my_model = BaseModel()
        current_time = datetime.now()
        my_model.save()
        self.assertEqual
        (my_model.updated_at, current_time + timedelta(seconds=1))

class TestSerializationBaseModel(unittest.TestCase):
    def test_to_dict(self):
        """ test serializes object BaseModel to dict """
        my_model = BaseModel()
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertIn('id', my_model_json)
        self.assertIn('created_at', my_model_json)
        self.assertIn('updated_at', my_model_json)


if __name__ == '__main__':
    unittest.main()
