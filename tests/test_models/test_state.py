#!/usr/bin/python3
"""Module for test state class"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):

    """create a new instance of state
    and verify it is an instance of BaseModel"""

    def test_create_instance(self):
        state = State()
        self.assertIsInstance(state, BaseModel)
    """create a new state with valid attributes"""

    def test_create_state_with_valid_details(self):
        state = State()
        state.name = "test@example.com"

        self.assertEqual(state.name, "test@example.com")

    """update state's attributes"""

    def test_update_state_details(self):
        state = State()
        state.email = "test@example.com"
        state.password = "password123"
        state.first_name = "John"
        state.last_name = "Doe"
        state.email = "new@example.com"
        state.password = "newpassword123"
        state.first_name = "Jane"
        state.last_name = "Smith"
        self.assertEqual(state.email, "new@example.com")
        self.assertEqual(state.password, "newpassword123")
        self.assertEqual(state.first_name, "Jane")
        self.assertEqual(state.last_name, "Smith")

    """save state's data to storage"""

    def test_save_state_data_to_storage(self):
        state = State()
        state.email = "test@example.com"
        state.password = "password123"
        state.first_name = "John"
        state.last_name = "Doe"
        state.save()

    """create a new state with empty attributes """

    def test_create_state_with_empty_details(self):
        state = State()
        self.assertEqual(state.name, "")

    """update state attributes """

    def test_update_state_name(self):
        state = State()
        state.name = "test@example.com"
        state.name = "new@example.com"
        self.assertEqual(state.name, "new@example.com")


if __name__ == "__main__":
    unittest.main()
