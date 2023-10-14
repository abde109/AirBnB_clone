#!/usr/bin/python3
"""FileStorage class handles the serialization and deserialization of instances"""
from json import loads, dumps
from os.path import exists
from ..user import User  # Modified import
from ..base_model import BaseModel  # Modified import

class FileStorage:
    """Storage class, allows for CRUD operations on objects"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all stored objects"""
        return self.__objects

    def new(self, obj):
        """Creates new object"""
        attr = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[attr] = obj  # store object instance, not dictionary

    def save(self):
        """Save objects to output.json"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()  # Call to_dict() to serialize

        with open(self.__file_path, "w") as f:
            json_object = dumps(serialized_objects)
            f.write(json_object)

    def reload(self):
        """Reads from output.json to load objects"""
        current_classes = {'BaseModel': BaseModel, 'User': User}
        if not exists(self.__file_path):
            with open(self.__file_path, "w") as g:
                g.write("{}")
        with open(self.__file_path, "r") as f:
            data = f.read()

        json_decode = loads(data)

        # Deserialize each object and store it in self.__objects
        for key, value in json_decode.items():
            class_name = value['__class__']
            if class_name in current_classes:
                self.__objects[key] = current_classes[class_name](**value)

