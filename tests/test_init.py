#!/usr/bin/python3
"""Unittest for base __init__ module"""



import unittest
from models.engine.file_storage import FileStorage



class Test_file_storage(unittest.TestCase):
    """test for file storage instance"""
    def test_instance(self):
        file_storage = FileStorage()
        self.assertIsInstance(file_storage, FileStorage)

    