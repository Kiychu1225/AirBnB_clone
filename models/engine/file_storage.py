#!/usr/bin/python3
"""
FileStorage Class definition
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


# Dictionary mapping class names to their corresponding classes
valid_classes = {'BaseModel': BaseModel,
                 'User': User,
                 'State': State,
                 'City': City,
                 'Amenity': Amenity,
                 'Place': Place,
                 'Review': Review}


class FileStorage():
    """Class used for file storage actions."""

    __file_path = "file.json"  # Path to the JSON file
    __objects = {}             # Dictionary to store objects

    def all(self):
        """Returns the dictionary of objects."""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the dictionary."""
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[obj_key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        with open(self.__file_path, 'w', encoding="utf-8") as fp:
            jdict_ = {}
            for k, v in self.__objects.items():
                dict_ = self.__objects[k].to_dict()
                jdict_[k] = dict_
            fp.write(json.dumps(jdict_))

    def reload(self):
        """Deserializes the JSON file to __objects."""
        dict_ = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as fp:
                str_ = fp.read()
                dict_ = json.loads(str_)
                for k, v in dict_.items():
                    class_ = v['__class__']
                    create_class = valid_classes[class_]
                    self.__objects[k] = create_class(**v)

