#!/usr/bin/python3
"""Defines a class to manage file storage for hbnb clone"""

import json


class FileStorage:
    """Manages storage of hbnb models in JSON format"""

    __file_path = 'file.json'
    __objects = {}
    def delete(self, obj=None):

        if obj is not None:
            class_name = obj.to_dict().get('__class__')
            obj_id = obj.id
            if class_name is not None and obj_id is not None:
                key = "{}.{}".format(class_name, obj_id)
                if key in FileStorage.__objects.keys():
                    del FileStorage.__objects[key]
                    self.save()

    def all(self, cls=None):
        """Returns the dictionary of models currently in storage"""

        if cls is None:
            return FileStorage.__objects
        else:
            tmp = {}
            for key, obj in FileStorage.__objects.items():
                parts = key.split('.')
                if len(parts) == 2:
                    obj_class_name = parts[0]

                if obj_class_name == cls.__name__:
                    tmp[key] = obj
            return tmp

    def new(self, obj):
        """Adds new object to the storage dictionary"""

        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to a file"""

        with open(FileStorage.__file_path, 'w') as f:
            tmp = {}
            tmp.update(FileStorage.__objects)
            for key, val in tmp.items():
                tmp[key] = val.to_dict()
            json.dump(tmp, f)

    def reload(self):
        """Loads storage dictionary from the file"""

        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.review import Review



        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            tmp = {}
            with open(FileStorage.__file_path, 'r') as f:
                tmp = json.load(f)
                for key, val in tmp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
