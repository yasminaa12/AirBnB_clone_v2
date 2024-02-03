#!/usr/bin/python3
""" State_Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
# SQLAlchemy modules
from sqlalchemy import Column, ForeignKey, Integer, Float, String


class Amenity(BaseModel, Base):
    '''Defines a class Amenity'''
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
