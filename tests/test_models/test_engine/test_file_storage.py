#!/usr/bin/python3
""" Module for test FileStorage class """
from models.engine.file_storage import FileStorage
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


if __name__ == '__main__':
    unittest.main()
