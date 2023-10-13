import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Class for testing the BaseModel class."""

    def test_init_no_dict(self):
        """Test initialization without passing a dictionary."""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_init_with_dict(self):
        """Test initialization with a dictionary argument."""
        model = BaseModel()
        model.name = "Test"
        model.my_number = 89
        model_json = model.to_dict()

        new_model = BaseModel(**model_json)
        self.assertEqual(new_model.id, model.id)
        self.assertEqual(new_model.name, "Test")
        self.assertEqual(new_model.my_number, 89)
        self.assertEqual(new_model.created_at, model.created_at)
        self.assertNotEqual(new_model, model)

    def test_str(self):
        """Test the __str__ method."""
        model = BaseModel()
        model.name = "Test"
        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected_str)

    def test_save(self):
        """Test the save method."""
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        new_updated_at = model.updated_at
        self.assertNotEqual(original_updated_at, new_updated_at)

    def test_to_dict(self):
        """Test the to_dict method."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
