#!/usr/bin/python3
"""Module for test Amenity class"""
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):

    """create a new instance of
    Review and verify it is an instance of BaseModel"""

    def test_create_instance(self):
        review = Amenity()
        self.assertIsInstance(review, BaseModel)
    """create an instance of Amenity with a name attribute"""

    def test_create_instance_with_name_attribute(self):
        amenity = Amenity(name="Pool")
        self.assertEqual(amenity.name, "Pool")

    """verify that the instance has an id attribute"""

    def test_verify_id_attribute(self):
        amenity = Amenity(name="Gym")
        self.assertTrue(hasattr(amenity, "id"))

    """verify that the instance has a created_at attribute"""

    def test_verify_created_at_attribute(self):
        amenity = Amenity(name="Spa")
        self.assertTrue(hasattr(amenity, "created_at"))

    """create an instance of Amenity without passing any arguments"""

    def test_create_instance_without_arguments(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    """create an instance of Amenity with a non-string name attribute"""

    def test_create_instance_with_non_string_name_attribute(self):
        amenity = Amenity(name=123)
        self.assertEqual(amenity.name, 123)

    """create an instance of Amenity with an empty name attribute"""

    def test_create_instance_with_empty_name_attribute(self):
        amenity = Amenity(name="")
        self.assertEqual(amenity.name, "")


if __name__ == "__main__":
    unittest.main()
