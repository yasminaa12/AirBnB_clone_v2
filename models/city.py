#!/usr/bin/python3
"""This is the City module."""
from models.base_model import BaseModel


class City(BaseModel):
    """Definition of the City class that inherits attributes and
       methods from the BaseModel class.
    """

    state_id = ""
    name = ""
