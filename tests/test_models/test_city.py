#!/usr/bin/python3
"""Module for test City class"""
from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):

    def test_create_instance(self):
        """create a new instance of City
        and verify it is an instance of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_create_city_with_valid_details(self):
        """create a new city with valid attributes"""
        city = City()
        city.name = "test@example.com"
        city.state_id = "password123"

        self.assertEqual(city.name, "test@example.com")
        self.assertEqual(city.state_id, "password123")

    def test_update_city_details(self):
        """update city's attributes"""
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

    def test_save_city_data_to_storage(self):
        """save city's data to storage"""
        city = City()
        city.email = "test@example.com"
        city.password = "password123"
        city.first_name = "John"
        city.last_name = "Doe"
        city.save()

    def test_create_city_with_empty_details(self):
        """create a new city with empty attributes """
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")


if __name__ == "__main__":
    unittest.main()
