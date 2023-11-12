#!/usr/bin/python3

"""User class inherited from BaseModel"""
import json
from models.base_model import BaseModel


class Review(BaseModel):
    """BaseMode subclass"""
    place_id = ""
    user_id = ""
    text = ""
