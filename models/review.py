#!/usr/bin/python3
"""This is a Class Module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This is the Review class, which inherits from the BaseModel class."""

    place_id = ""
    user_id = ""
    text = ""
