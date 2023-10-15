#!/usr/bin/python3


from models.base_model import BaseModel
from models.state import State

import unittest


class TestState(unittest.TestCase):

    # create a new instance of Review and verify it is an instance of BaseModel
    def test_create_instance(self):
        review = State()
        self.assertIsInstance(review, BaseModel)
    # create a new instance of State with a name attribute

    def test_create_instance_with_name_attribute(self):
        state = State(name="California")
        self.assertEqual(state.name, "California")

    # check that the State instance has a name attribute
    def test_check_name_attribute(self):
        state = State(name="California")
        self.assertTrue(hasattr(state, "name"))

    # check that the State instance has an id attribute
    def test_check_id_attribute(self):
        state = State(name="California")
        self.assertTrue(hasattr(state, "id"))

    # Create a new instance of State without a name attribute
    def test_create_instance_without_name_attribute(self):
        state = State()
        self.assertTrue(hasattr(state, "name"))

    # create a new instance of State with an empty name attribute
    def test_create_instance_with_empty_name_attribute(self):
        state = State(name="")
        self.assertEqual(state.name, "")

    # create a new instance of State with a name attribute that is too long
    def test_create_instance_with_long_name_attribute(self):
        state = State(
            name="This is a very long name that exceeds the maximum allowed length")
        self.assertEqual(
            state.name,
            "This is a very long name that exceeds the maximum allowed length")
