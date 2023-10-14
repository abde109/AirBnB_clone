#!/usr/bin/python3
"""
This module defines the FileStorage class for handling storage of objects.
"""

from json import loads, dumps
from os.path import exists
from models.user import User
from models.base_model import BaseModel

class FileStorage:
    """
    FileStorage class for serializing and deserializing instances.
    """
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Create a new object.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """
        Serialize objects to the JSON file.
        """
        with open(self.__file_path, "w") as f:
            dumps(self.__objects, f)

    def reload(self):
        """
        Deserialize objects from the JSON file.
        """
        if exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                self.__objects = loads(f.read())

            current_classes = {'BaseModel': BaseModel, 'User': User}

            for key, obj_dict in self.__objects.items():
                class_name = obj_dict["__class__"]
                if class_name in current_classes:
                    self.__objects[key] = current_classes[class_name](**obj_dict)
