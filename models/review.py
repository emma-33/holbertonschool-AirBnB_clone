#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """Create a Class Review """
    place_id = ""
    user_id = ""
    text = ""
