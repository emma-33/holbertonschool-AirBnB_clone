#!/usr/bin/python3
from models.base_model import BaseModel


class State(BaseModel):
    """Create a Class State"""
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
