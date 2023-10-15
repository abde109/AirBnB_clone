#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.
"""
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


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


if __name__ == "__main__":
    unittest.main()
