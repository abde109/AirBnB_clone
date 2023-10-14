#!/usr/bin/python3
"""
This module contains the FileStorage class for managing the storage
of objects to a JSON file and reloading objects from the JSON file.
"""
from json import loads, dumps
from os.path import exists
from models.user import User
from models.base_model import BaseModel

class FileStorage:
    """
    FileStorage class, allows for CRUD (Create, Read, Update, Delete) operations of objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns all stored objects as a dictionary.
        """
        return self.__objects

    def new(self, obj):
        """
        Creates a new object and adds it to the __objects dictionary.
        """
        attr = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[attr] = obj.to_dict()

    def save(self):
        """
        Serializes objects to a JSON file.
        """
        with open(self.__file_path, "w") as f:
            json_object = dumps(self.__objects)
            f.write(json_object)

    def reload(self):
        """
        Deserializes objects from a JSON file and loads them into __objects.
        """
        current_classes = {'BaseModel': BaseModel, 'User': User}
        if not exists(self.__file_path):
            with open(self.__file_path, "w") as g:
                g.write("{}")
        with open(self.__file_path, "r") as f:
            data = f.read()
        json_decode = loads(data)
        self.__objects = json_decode
