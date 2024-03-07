#!/usr/bin/python3
from models.base_model import BaseModel
"""User module"""

class User(BaseModel):
    """Class User inheriting from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""