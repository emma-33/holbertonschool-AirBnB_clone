#!/usr/bin/python3
""" Module for test FileStorage class """
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest

""" class test DefineFileStorage """


class TestDefineFileStorage(unittest.TestCase):
    def test_instantiation(self):
        """ test new instance of File storage """
        file_path = "file.json"
        storage = FileStorage(file_path)
        self.assertIsInstance(storage, FileStorage)

    def test_instantiation_withoutfile(self):
        """ test new instance of Filestorage without file """
        with self.assertRaises(TypeError):
            FileStorage()

    def test_instantiation_with_int_file_path(self):
        """ test new instance of Filestorage with integer file """
        storage = FileStorage(18)
        self.assertIsInstance(storage, FileStorage)

    def test_instantiation_with_float_file_path(self):
        """ test new instance of Filestorage with float file """
        storage = FileStorage(18.5)
        self.assertIsInstance(storage, FileStorage)

    def test_instantiation_with_list_file_path(self):
        """ test new instance of Filestorage with list file """
        storage = FileStorage([20, 25, 50])
        self.assertIsInstance(storage, FileStorage)

    def test_instantiation_with_dict_file_path(self):
        """ test new instance of Filestorage with dict file """
        storage = FileStorage({"key: value"})
        self.assertIsInstance(storage, FileStorage)

    def test_instantiation_with_tuple_file_path(self):
        """ test new instance of Filestorage with tuple file """
        storage = FileStorage((20, 40, 60, 90))
        self.assertIsInstance(storage, FileStorage)

    def test_instantiation_with_none_file_path(self):
        """ test new instance of Filestorage with none file """
        storage = FileStorage(None)
        self.assertIsInstance(storage, FileStorage)


""" Class Test verify attributes file and objects """


class TestAttributes(unittest.TestCase):
    def test_filepath_attribute(self):
        """ test file_path private attribute """
        file_path = "file.json"
        storage = FileStorage(file_path)
        self.assertEqual(storage._FileStorage__file_path, file_path)

    def test_objects_attribute(self):
        """ test objects private attribute is correctly initialized """
        file_path = "file.json"
        storage = FileStorage(file_path)
        self.assertIsInstance(storage._FileStorage__objects, dict)
        self.assertEqual(len(storage._FileStorage__objects), 0)

    def test_objects_notempty(self):
        """ test objects not empty """
        file_path = "file.json"
        storage = FileStorage(file_path)
        object1 = BaseModel()
        storage.new(object1)
        key = "{}.{}".format(object1.__class__.__name__, object1.id)
        self.assertIn(key, storage._FileStorage__objects)
        self.assertEqual(storage._FileStorage__objects[key], object1)


class TestInstancesStoraged(unittest.TestCase):
    def test_objects_storaged(self):
        """ tests return objects storaged """
        file_path = "file.json"
        storage = FileStorage(file_path)
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj3 = BaseModel()
        storage.new(obj1)
        storage.new(obj2)
        storage.new(obj3)
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertIn("BaseModel." + obj1.id, all_objects)
        self.assertIn("BaseModel." + obj2.id, all_objects)
        self.assertIn("BaseModel." + obj3.id, all_objects)


""" Class Test Serialization objects to the JSON file """


class TestSerializationToJSON(unittest.TestCase):
    def test_serialize_objects(self):
        file_path = "file.json"
        storage = FileStorage(file_path)
        obj = BaseModel()

        storage.new(obj)

        storage.save()

        self.assertTrue(os.path.exists(file_path))

        with open(file_path, "r") as json_file:
            json_data = json.load(json_file)

        self.assertIn("BaseModel.{}".format(obj.id), json_data)

        os.remove(file_path)
