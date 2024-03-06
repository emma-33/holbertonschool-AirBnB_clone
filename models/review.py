#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """Create a Class Review """
    def __init__(self, name, place_id, user_id, text, *args, **kwargs):
        """ Initialisation Review attributes """
        super().__init__(*args, **kwargs)
        self.name = name
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
