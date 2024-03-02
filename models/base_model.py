#!/usr/bin/pyhton3
import uuid
from datetime import datetime


class BaseModel:
    """Create a Class BaseModel"""
    def __init__(self):
        """Init attribute"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Representation to a string"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Add a dict"""
        obj_dict = self.__dict__
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()

        return obj_dict
