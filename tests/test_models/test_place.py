#!/usr/bin/python3
"""
Module for unittests for the Place class
"""
import unittest
import os
import models
from models.place import Place


class TestPlaceCreation(unittest.TestCase):
    """Test class for instantiating Place"""

    def setUp(self):
        """
        Set up test environment
        """
        self.file = 'file.json'  # Path to the JSON file
        try:
            os.remove(self.file)
        except:
            pass
        self.x = Place()  # Create an instance of Place
        self.validAttributes = {
            'city_id': str,
            'user_id': str,
            'name': str,
            'description': str,
            'number_rooms': int,
            'max_guest': int,
            'price_by_night': int,
            'latitude': float,
            'longitude': float,
            'amenity_ids': list,
        }  # Dictionary of valid attributes and their types
        self.storage = models.storage  # Instance of FileStorage

    def tearDown(self):
        """
        Clean up test environment
        """
        try:
            os.remove(self.file)
        except:
            pass

    def createPlace(self):
        """
        Create a Place object with specific attributes for testing
        """
        self.ex = Place()
        self.ex.city_id = "23asdk"
        self.ex.user_id = "asdfoie"
        self.ex.name = "John"
        self.ex.description = "Nice"
        self.ex.number_rooms = 32
        self.ex.number_bathrooms = 3
        self.ex.max_guest = 4
        self.ex.price_by_night = 199
        self.ex.latitude = 13.2323
        self.ex.longitude = 165.2323
        self.ex.amenity_ids = ['amenity1',
                               'amenity2',
                               'amenity3']

    def test_has_correct_class_name(self):
        """
        Test if the class name is correct
        """
        self.assertEqual('Place', self.x.__class__.__name__)

    def test_empty_has_attrs(self):
        """
        Test if an empty Place has the required attributes
        """
        for k in self.validAttributes:
            self.assertTrue(hasattr(self.x, k))

    def test_empty_attrs_type(self):
        """
        Test if attributes of an empty Place have correct types
        """
        for k, v in self.validAttributes.items():
            test_type = type(getattr(self.x, k))
            self.assertEqual(test_type, v)

    def test_added_attrs(self):
        """
        Test if additional attributes can be added to a Place
        """
        self.createPlace()
        self.assertEqual(self.ex.city_id, "23asdk")
        self.assertEqual(self.ex.user_id, "asdfoie")
        self.assertEqual(self.ex.name, "John")
        self.assertEqual(self.ex.description, "Nice")
        self.assertEqual(self.ex.number_rooms, 32)
        self.assertEqual(self.ex.number_bathrooms, 3)
        self.assertEqual(self.ex.max_guest, 4)

    def test_check_custom_attrs(self):
        """
        Test if custom attributes can be added to a Place
        """
        self.x.custom_attr = "Nga"
        self.assertEqual(self.x.custom_attr, "Nga")
        self.assertIsInstance(self.x.custom_attr, str)

    # #TODO: This fails occasionally
    def test_save_time_change(self):
        """
        Test if saving a Place changes its 'updated_at' time
        """
        old_time = self.x.updated_at
        self.x.save()
        self.assertNotEqual(self.x.updated_at, old_time)

    def test_new_dict(self):
        """
        Test if a new Place can be created from a dictionary
        """
        self.createPlace()
        dict_ = self.ex.to_dict()
        self.y = Place(**dict_)
        self.assertEqual(self.ex.name, self.y.name)

    def test_new_dict_attr_types(self):
        """
        Test if attributes of a new Place created from a dictionary have correct types
        """
        self.createPlace()
        dict_ = self.ex.to_dict()
        self.y = Place(**dict_)
        for k, v in self.validAttributes.items():
            test_type = type(getattr(self.y, k))
            self.assertEqual(test_type, v)

    def test_save(self):
        """
        Test if storage saves the Place correctly
        """
        self.assertIsInstance(self.storage._FileStorage__objects, dict)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file))
        self.assertTrue(os.stat(self.file).st_size != 0)

    def test_reload(self):
        """
        Test if storage reloads the Place correctly
        """
        x_id = self.x.id
        x_id_key = "{}.{}".format(self.x.__class__.__name__, self.x.id)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertEqual(x_id,
                         self.storage._FileStorage__objects[x_id_key].id)

