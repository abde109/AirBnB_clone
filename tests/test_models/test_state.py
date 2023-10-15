#!/usr/bin/python3
"""Module for test state class"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):

    def test_create_instance(self):
        """create a new instance of state
        and verify it is an instance of BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_create_state_with_valid_details(self):
        """create a new state with valid attributes"""
        state = State()
        state.name = "test@example.com"

        self.assertEqual(state.name, "test@example.com")

    def test_update_state_details(self):
        """update state's attributes"""
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

    def test_save_state_data_to_storage(self):
        """save state's data to storage"""
        state = State()
        state.email = "test@example.com"
        state.password = "password123"
        state.first_name = "John"
        state.last_name = "Doe"
        state.save()

    def test_create_state_with_empty_details(self):
        """create a new state with empty attributes """
        state = State()
        self.assertEqual(state.name, "")

    def test_update_state_name(self):
        """update state attributes """
        state = State()
        state.name = "test@example.com"
        state.name = "new@example.com"
        self.assertEqual(state.name, "new@example.com")


if __name__ == "__main__":
    unittest.main()
