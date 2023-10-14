#!/usr/bin/python3
"""my very first custom backend orm :)"""
from json import loads, dumps


class FileStorage:
    """"Storage class, allows for crud of objects"""
    __file_path = "output.json"
    _objects = {}

    def all(self):
        """returns all stored objects"""
        return self._objects

    def new(self, obj):
        """creates new object"""
        self._objects[obj.__class__.__name__ +
                      '.' + str(obj.id)] = obj.to_dict()

    def save(self):
        """save objects to output.json"""
        f = open(self.__file_path, "w")

        json_object = dumps(self._objects)
        with f:
            f.write(json_object)
        f.close()

    def reload(self):
        """reads from output.json to load objects"""
        f = open(self.__file_path, "r")

        with f:
            data = f.read()
        json_decode = loads(data)
        self._objects = json_decode
        f.close()
