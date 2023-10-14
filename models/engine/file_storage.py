#!/usr/bin/python3
"""
This module contains the FileStorage class for managing storage of objects.
"""

from json import load, dump
from os.path import exists

class FileStorage:
    """FileStorage class for serializing and deserializing instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all stored objects."""
        return self.__objects

    def new(self, obj):
        """Create new object."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize objects to the JSON file."""
        save_dict = {}
        for key, obj in self.__objects.items():
            save_dict[key] = obj.to_dict()

        with open(self.__file_path, "w") as f:
            dump(save_dict, f)

    def reload(self):
        """Deserialize objects from the JSON file."""
        if exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                loaded_dict = load(f)

            for key, obj_dict in loaded_dict.items():
                class_name = obj_dict["__class__"]
                if class_name in models.__dict__:
                    self.__objects[key] = models.__dict__[class_name](**obj_dict)
