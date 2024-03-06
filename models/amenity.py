#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Create a Class Amenity"""
    def __init__(self, name, *args, **kwargs):
        """ Initialisation attributes Amenity """
        super().__init__(*args, **kwargs)
        self.name = name
