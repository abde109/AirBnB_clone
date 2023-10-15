#!/usr/bin/python3
"""Module for test User class"""
from models.base_model import BaseModel
from models.user import User
import unittest


class TestUser(unittest.TestCase):

    def test_create_instance(self):
        """create a new instance of Review
        and verify it is an instance of BaseModel"""
        review = User()
        self.assertIsInstance(review, BaseModel)

    def test_create_user_with_valid_details(self):
        """create a new user with valid email,
        password, first_name and last_name"""
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_update_user_details(self):
        """update user's email, password, first_name and last_name"""
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"
        user.email = "new@example.com"
        user.password = "newpassword123"
        user.first_name = "Jane"
        user.last_name = "Smith"
        self.assertEqual(user.email, "new@example.com")
        self.assertEqual(user.password, "newpassword123")
        self.assertEqual(user.first_name, "Jane")
        self.assertEqual(user.last_name, "Smith")

    def test_save_user_data_to_storage(self):
        """save user's data to storage"""
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"
        user.save()

    def test_create_user_with_empty_details(self):
        """create a new user with empty email,
        password, first_name and last_name"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == "__main__":
    unittest.main()
