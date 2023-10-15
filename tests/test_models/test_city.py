#!/usr/bin/python3
"""Module for test City class"""
from models.base_model import BaseModel
from models.city import City
import models


import unittest


class TestCity(unittest.TestCase):

    """create a new instance of
    Review and verify it is an instance of BaseModel"""

    def test_create_instance(self):
        review = City()
        self.assertIsInstance(review, BaseModel)
    """create a new City instance with state_id and name attributes"""

    def test_create_city_with_state_id_and_name(self):
        city = City(state_id="123", name="New York")
        self.assertEqual(city.state_id, "123")
        self.assertEqual(city.name, "New York")

    """City instance has id, created_at, and updated_at attributes"""

    def test_city_instance_attributes(self):
        city = City(state_id="123", name="New York")
        self.assertIsNotNone(city.created_at)
        self.assertIsNotNone(city.updated_at)

    """City instance can be saved to storage"""

    def test_save_city_to_storage(self):
        city = City(state_id="123", name="New York")
        models.storage.save()
        self.assertIn(city, models.storage.all().values())

    """create a new City instance with empty state_id and name attributes"""

    def test_create_city_with_empty_state_id_and_name(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    """create a new City instance with state_id and empty name attributes"""

    def test_create_city_with_state_id_and_empty_name(self):
        city = City(state_id="123")
        self.assertEqual(city.state_id, "123")
        self.assertEqual(city.name, "")

    """create a new City instance with None state_id and name attributes"""

    def test_create_city_with_none_state_id_and_name(self):
        city = City(state_id=None, name=None)
        self.assertIsNone(city.state_id)
        self.assertIsNone(city.name)
