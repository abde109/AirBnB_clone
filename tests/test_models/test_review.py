#!/usr/bin/python3
"""Module for test Review class"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):

    """create a new instance of review
    and verify it is an instance of BaseModel"""

    def test_create_instance(self):
        review = Review()
        self.assertIsInstance(review, BaseModel)
    """create a new review with valid attributes"""

    def test_create_review_with_valid_details(self):
        review = Review()
        review.name = "test@example.com"

        self.assertEqual(review.name, "test@example.com")

    """update review's attributes"""

    def test_update_review_details(self):
        review = Review()
        review.email = "test@example.com"
        review.password = "password123"
        review.first_name = "John"
        review.last_name = "Doe"
        review.email = "new@example.com"
        review.password = "newpassword123"
        review.first_name = "Jane"
        review.last_name = "Smith"
        self.assertEqual(review.email, "new@example.com")
        self.assertEqual(review.password, "newpassword123")
        self.assertEqual(review.first_name, "Jane")
        self.assertEqual(review.last_name, "Smith")

    """save review's data to storage"""

    def test_save_review_data_to_storage(self):
        review = Review()
        review.email = "test@example.com"
        review.password = "password123"
        review.first_name = "John"
        review.last_name = "Doe"
        review.save()

    """create a new review with empty attributes """

    def test_create_review_with_empty_details(self):
        review = Review()
        self.assertEqual(review.name, "")


if __name__ == "__main__":
    unittest.main()
