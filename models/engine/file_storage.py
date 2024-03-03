#!/usr/bin/python3
""" Import module class """
import json


class FileStorage


""" Create a Class FileStorage that serializes
instances to a JSON file and deserializes JSON file to instances"""


def __init__(self, file_path):
    """ Init private attributes """
    self.__file_path = file_path
    self.__objects = {}

    @property
    def get_file(self):
        """Getter for file_path"""
        return self.__file_path

    @setter
    def set_file(self, value):
        """Setter for file_path"""
        self.__file_path = value

    @property
    def objects(self):
        """Getter for objects"""
        return self.__objects

    @objects.setter
    def objects(self, value):
        """Setter for objects"""
        self.__objects = value

    def all(self):
        """ return instances storaged """
        return self.__objects

    def new(self, obj):
        """ Add a new object to objects dictionary """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serialize __objects to the JSON file (path: __file_path) """
        with open(self.__file_path, "w") as jsonfile:
            json.dump(self.__objects, jsonfile)

    def reload(self):
        """ Deserialize the object from JSON file """
        try:
            with open(self.__file_path, "r") as jsonfile:
                self.__objects = json.load(jsonfile)
        except FileNotFoundError:
            pass
