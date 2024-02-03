#!/usr/bin/python3
""" Place Module for HBNB_project """
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from os import environ
from sqlalchemy.orm import relationship

metadata = Base.metadata
place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id', ondelete='CASCADE')),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id', ondelete='CASCADE')))


class Place(BaseModel, Base):
    """Representation a place
    -Attributes:
        __tablename__ (str): Place MySQL table name

        -city_id (string): ID of city.
        -user_id (string): ID of user.
        -name (string): name of Place.
        -description (string): description of place.
        -number_rooms (integer): number of rooms in place.
        -number_bathrooms (integer): number of bathrooms in place.
        -max_guest (integer): maximum number of guests allowed in a place.
        -price_by_night (integer): price of room per night.
        -latitude (float): latitude of place on a map.
        -longitude (float): longitude of place on a map.
        -amenity_ids (list (of string)): list of Amenity.id of place.
    """

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id", ondelete='CASCADE'),
                     nullable=False)
    user_id = Column(String(60), ForeignKey("users.id",
                     ondelete='CASCADE'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place", cascade="delete")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False)

    if environ.get('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """
            Returns the list of Review instances with place_id equals
            to the current Place.id.
            """
            from models.review import Review
            return [review for review in models.storage.all(Review).values()
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """
            Returns the list of Amenity instances based on the attribute
            amenity_ids that contains all Amenity.id linked to the Place.
            """
            return [amenity for amenity in models.storage.all(Amenity).values()
                    if amenity.place_id == self.id]

        @amenities.setter
        def amenities(self, obj):
            """
            Handles append method for adding an Amenity.id to the attribute
            amenity_ids. This method should accept only Amenity object,
            otherwise do nothing.
            """
            if not isinstance(obj, Amenity):
                return
            self.amenity_ids.append(obj.id)
