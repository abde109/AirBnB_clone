

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):

    # create a new instance of Review and verify it is an instance of BaseModel
    def test_create_instance(self):
        review = Review()
        self.assertIsInstance(review, BaseModel)

    # set the name attribute of a Review instance and verify it is set
    # correctly
    def test_set_name_attribute(self):
        review = Review()
        review.name = "Test Review"
        self.assertEqual(review.name, "Test Review")

    # call the to_dict method on a Review instance and verify the returned
    # dictionary contains the expected keys and values
    def test_to_dict_method(self):
        review = Review()
        review.name = "Test Review"
        review_dict = review.to_dict()
        expected_dict = {
            'id': review.id,
            'created_at': review.created_at.isoformat(),
            'updated_at': review.updated_at.isoformat(),
            '__class__': 'Review',
            'name': 'Test Review'
        }
        self.assertDictEqual(review_dict, expected_dict)

    # create a new instance of Review with no arguments and verify that the
    # id, created_at, and updated_at attributes are set correctly
    def test_create_instance_with_no_arguments(self):
        review = Review()
        self.assertIsNotNone(review.id)
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)
