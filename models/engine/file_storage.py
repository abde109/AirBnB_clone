#!/usr/bin/python3
"""my very first custom backend orm :)"""
from json import loads, dumps
from os.path import exists


class FileStorage:
    """"Storage class, allows for crud of objects"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all stored objects"""
        return self.__objects

    def new(self, obj):
        """creates new object"""
        attr = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[attr] = obj.to_dict()

    def save(self):
        """save objects to output.json"""
        f = open(self.__file_path, "w")

        json_object = dumps(self.__objects)
        with f:
            f.write(json_object)
        f.close()

    def reload(self):
        """reads from output.json to load objects"""
        if not exists(self.__file_path):
            g = open(self.__file_path, "w")
            g.write("{}")
            g.close()
        f = open(self.__file_path, "r")

        with f:
            data = f.read()
        json_decode = loads(data)
        self.__objects = json_decode
        f.close()
