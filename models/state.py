#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import environ
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


# The State class is defined with BaseModel and Base as its parent classes,
# This means that State inherits all the attributes & methods of these classes.
class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    """
    This creates a column named “name” that stores strings of up to 128
    characters. nullable=False means this column cannot be empty.
    """
    cities = relationship("City",
                          backref="state",
                          cascade="all, delete-orphan",
                          passive_deletes=True)

    if environ.get('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            return [city for city in models.storage.all(
                City).values() if city.state_id == self.id]
