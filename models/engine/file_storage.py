#!/usr/bin/python3
from json import loads, dumps


class FileStorage:

    __file_path = "output.json"
    _objects = {}

    def all(self):
        return self._objects

    def new(self, obj):
        self._objects[obj.__class__.__name__] = obj.id

    def save(self):
        f = open(self.__file_path, "w")

        json_object = dumps(self._objects)
        with f:
            f.write(json_object)
        f.close()

    def reload(self):
        f = open(self.__file_path, "r")

        with f:
            data = f.read()
        json_decode = loads(data)
        self._objects = json_decode
        f.close()
