#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.
"""
import models
import unittest
import os
from models.engine.file_storage import FileStorage
from models.user import User
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State
from models.place import Place
import json


class TestFileStorage(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        """Test instantiating FileStorage with no arguments"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        """Test instantiating FileStorage with an argument"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        """Test the type of __file_path attribute"""
        self.assertEqual(str, type(models.storage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        """Test the type of __objects attribute"""
        self.assertEqual(dict, type(models.storage._FileStorage__objects))

    def test_storage_initializes(self):
        """Test if storage is an instance of FileStorage"""
        self.assertEqual(type(models.storage), FileStorage)

    def test_all(self):
        """Test the 'all' method"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        """Test the 'all' method with an argument"""
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        """Test the 'new' method"""
        bm = BaseModel()

        models.storage.new(bm)
        models.storage.save()
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())

    def test_new_with_args(self):
        """Test the 'new' method with invalid arguments"""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        """Test the 'new' method with None as an argument"""
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        """Test the 'save' method"""
        bm = BaseModel()

        models.storage.new(bm)

        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)

    def test_save_with_arg(self):
        """Test the 'save' method with an argument"""
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        """Test the 'reload' method"""
        bm = BaseModel()
        models.storage.new(bm)
        models.storage.save()
        models.storage.reload()
        objs = models.storage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)

    def test_reload_with_arg(self):
        """Test the 'reload' method with an argument"""
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def setUp(self):
        """Establishes test config for class."""
        self.b1 = BaseModel()
        self.a1 = Amenity()
        self.c1 = City()
        self.p1 = Place()
        self.r1 = Review()
        self.s1 = State()
        self.u1 = User()
        self.storage = FileStorage()
        self.storage.save()
        if os.path.exists("file.json"):
            pass
        else:
            os.mknod("file.json")

    def tearDown(self):
        """Dismantles the testing environment."""

        del self.b1
        del self.a1
        del self.c1
        del self.p1
        del self.r1
        del self.s1
        del self.u1
        del self.storage
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Checks everything"""
        obj = self.storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, self.storage._FileStorage__objects)

    def test_storage_empty(self):
        """Checks if storage is not empty"""

        self.assertIsNotNone(self.storage.all())

    def test_storage_all_type(self):
        """Checks the type of storage"""

        self.assertEqual(dict, type(self.storage.all()))

    def test_new(self):
        """Checks the new user"""
        obj = self.storage.all()
        self.u1.id = 1234
        self.u1.name = "Julien"
        self.storage.new(self.u1)
        key = "{}.{}".format(self.u1.__class__.__name__, self.u1.id)
        self.assertIsNotNone(obj[key])

    def test_check_json_loading(self):
        """ Checks if methods from Storage Engine works."""

        with open("file.json") as f:
            dic = json.load(f)

            self.assertEqual(isinstance(dic, dict), True)

    def test_file_existence(self):
        """
        Checks if methods from Storage Engine works.
        """

        with open("file.json") as f:
            self.assertTrue(len(f.read()) > 0)

    def test_docstrings(self):
        """Check the docString each function"""

        self.assertTrue(FileStorage.all.__doc__)
        self.assertTrue(hasattr(FileStorage, 'all'))
        self.assertTrue(FileStorage.new.__doc__)
        self.assertTrue(hasattr(FileStorage, 'new'))
        self.assertTrue(FileStorage.save.__doc__)
        self.assertTrue(hasattr(FileStorage, 'save'))
        self.assertTrue(FileStorage.reload.__doc__)
        self.assertTrue(hasattr(FileStorage, 'reload'))

    def test_save_then_reload(self):
        obj = models.base_model.BaseModel()
        models.storage.new(obj)
        models.storage.save()
        del models.storage.all()["{}.{}".format(obj.__class__.__name__,
                                                obj.id)]
        models.storage.reload()
        self.assertIn(
            "{}.{}".format(obj.__class__.__name__, obj.id),
            models.storage.all()
        )


if __name__ == "__main__":
    unittest.main()
