#!/usr/bin/python3
"""Module for test Amenity class"""
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):

    """create a new instance of amenity
    and verify it is an instance of BaseModel"""

    def test_create_instance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
    """create a new amenity with valid attributes"""

    def test_create_amenity_with_valid_details(self):
        amenity = Amenity()
        amenity.name = "test@example.com"
        amenity.state_id = "password123"

        self.assertEqual(amenity.name, "test@example.com")
        self.assertEqual(amenity.state_id, "password123")

    """update amenity's attributes"""

    def test_update_amenity_details(self):
        amenity = Amenity()
        amenity.email = "test@example.com"
        amenity.password = "password123"
        amenity.first_name = "John"
        amenity.last_name = "Doe"
        amenity.email = "new@example.com"
        amenity.password = "newpassword123"
        amenity.first_name = "Jane"
        amenity.last_name = "Smith"
        self.assertEqual(amenity.email, "new@example.com")
        self.assertEqual(amenity.password, "newpassword123")
        self.assertEqual(amenity.first_name, "Jane")
        self.assertEqual(amenity.last_name, "Smith")

    """save amenity's data to storage"""

    def test_save_amenity_data_to_storage(self):
        amenity = Amenity()
        amenity.email = "test@example.com"
        amenity.password = "password123"
        amenity.first_name = "John"
        amenity.last_name = "Doe"
        amenity.save()

    """create a new amenity with empty attributes """

    def test_create_amenity_with_empty_details(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == "__main__":
    unittest.main()
