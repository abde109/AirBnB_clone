#!/usr/bin/python3
"""Module for test City class"""
from models.base_model import BaseModel
from models.city import City
import models


import unittest


class TestCity(unittest.TestCase):
    """create a new instance of City
    and verify it is an instance of BaseModel"""

    def test_create_instance(self):
        city = City()
        self.assertIsInstance(city, BaseModel)
    """create a new city with valid attributes"""

    def test_create_city_with_valid_details(self):
        city = City()
        city.name = "test@example.com"
        city.state_id = "password123"

        self.assertEqual(city.name, "test@example.com")
        self.assertEqual(city.state_id, "password123")

    """update city's attributes"""

    def test_update_city_details(self):
        city = City()
        city.email = "test@example.com"
        city.password = "password123"
        city.first_name = "John"
        city.last_name = "Doe"
        city.email = "new@example.com"
        city.password = "newpassword123"
        city.first_name = "Jane"
        city.last_name = "Smith"
        self.assertEqual(city.email, "new@example.com")
        self.assertEqual(city.password, "newpassword123")
        self.assertEqual(city.first_name, "Jane")
        self.assertEqual(city.last_name, "Smith")

    """save city's data to storage"""

    def test_save_city_data_to_storage(self):
        city = City()
        city.email = "test@example.com"
        city.password = "password123"
        city.first_name = "John"
        city.last_name = "Doe"
        city.save()

    """create a new city with empty attributes """

    def test_create_city_with_empty_details(self):
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")


if __name__ == "__main__":
    unittest.main()
