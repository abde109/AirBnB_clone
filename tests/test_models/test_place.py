
from models.place import Place
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
import models


class TestPlace(unittest.TestCase):

    # create a new instance of Place and verify that it is a subclass of
    # BaseModel
    def test_new_instance_is_subclass_of_BaseModel(self):
        place = Place()
        self.assertIsInstance(place, BaseModel)

    # set attributes of a Place instance and verify that they are saved
    # correctly
    def test_set_attributes_are_saved_correctly(self):
        place = Place()
        place.city_id = "123"
        place.user_id = "456"
        place.name = "Test Place"
        place.description = "This is a test place"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["1", "2", "3"]

        self.assertEqual(place.city_id, "123")
        self.assertEqual(place.user_id, "456")
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.description, "This is a test place")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["1", "2", "3"])

    # call save() on a Place instance and verify that updated_at is updated
    # and the instance is saved to storage
    def test_save_updates_updated_at_and_saves_instance_to_storage(self):
        place = Place()
        original_updated_at = place.updated_at

        place.save()

        self.assertNotEqual(place.updated_at, original_updated_at)
        self.assertIn(place, models.storage.all().values())

    # create a new Place instance with no arguments and verify that the id,
    # created_at, and updated_at attributes are set correctly
    def test_new_instance_with_no_arguments_sets_attributes_correctly(self):
        place = Place()

        self.assertIsNotNone(place.id)
        self.assertIsNotNone(place.created_at)
        self.assertIsNotNone(place.updated_at)
