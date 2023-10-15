#!/usr/bin/python3
"""Module for test Review class"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):

    def test_create_instance(self):
        """create a new instance of review
        and verify it is an instance of BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_create_review_with_valid_details(self):
        """create a new review with valid attributes"""
        review = Review()
        review.text = "test@example.com"

        self.assertEqual(review.text, "test@example.com")

    def test_update_review_details(self):
        """update review's attributes"""
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

    def test_save_review_data_to_storage(self):
        """save review's data to storage"""
        review = Review()
        review.email = "test@example.com"
        review.password = "password123"
        review.first_name = "John"
        review.last_name = "Doe"
        review.save()

    def test_create_review_with_empty_details(self):
        """create a new review with empty attributes """
        review = Review()
        self.assertEqual(review.text, "")


if __name__ == "__main__":
    unittest.main()
