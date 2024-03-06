#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """Create a Class City"""
    def __init__(self, name, state_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.state_id = state_id
