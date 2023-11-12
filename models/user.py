#!/usr/bin/python3

"""User class inherited from BaseModel"""
import json
from models.base_model import BaseModel


class User(BaseModel):
    """BaseMode subclass"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
