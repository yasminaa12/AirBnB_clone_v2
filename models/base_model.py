#!/usr/bin/python3
"""This is the Base Model module"""

import uuid
from models import storage
from datetime import datetime


class BaseModel:
    """This is the BaseModel class that defines common
       attributes and methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """Code block for initializing the class.
        Args:
            *args: unused
            **kwargs (dict): Dictionnary containing wanted attributes
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)

    def __str__(self):
        """Method to obtain a string representation
        of the selected attribute.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Method for refreshing the 'updated_at' public
           instance attribute with the current timestamp.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Method to retrieve a dictionary containing
        all attributes and their values for the instance.
        """
        new_dict = {}
        for k, v in self.__dict__.items():
            if k in ["created_at", "updated_at"]:
                new_dict[k] = v.isoformat()
            else:
                new_dict[k] = v
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
