#!/usr/bin/python3
"""
Module for unittests for the Amenity class
"""
import unittest
import os
import models
from models.amenity import Amenity


class TestAmenityEmptyCreation(unittest.TestCase):
    """Test class for instantiating Amenity"""

    def setUp(self):
        """
        Set up test environment
        """
        self.file = 'file.json'  # Path to the JSON file
        try:
            os.remove(self.file)
        except:
            pass
        self.x = Amenity()  # Create an instance of Amenity
        self.validAttributes = {
            'name': str,
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

    def test_user_has_correct_class_name(self):
        """
        Test if the class name is correct
        """
        self.assertEqual('Amenity', self.x.__class__.__name__)

    def test_empty_amenity_has_attrs(self):
        """
        Test if an empty amenity has the required attributes
        """
        for k in self.validAttributes:
            self.assertTrue(hasattr(self.x, k))

    def test_empyt_amenity_attrs_type(self):
        """
        Test if attributes of an empty amenity have correct types
        """
        for k, v in self.validAttributes.items():
            test_type = type(getattr(self.x, k))
            self.assertEqual(test_type, v)

    def test_amenity_added_attrs(self):
        """
        Test if additional attributes can be added to an amenity
        """
        self.x.name = "pool"
        self.assertEqual(self.x.name, "pool")

    def test_check_custom_attrs(self):
        """
        Test if custom attributes can be added to an amenity
        """
        self.x.custom_attr = "Test"
        self.assertEqual(self.x.custom_attr, "Test")
        self.assertIsInstance(self.x.custom_attr, str)

    # TODO: This fails occasionally
    def test_save_time_change(self):
        """
        Test if saving an amenity changes its 'updated_at' time
        """
        old_time = self.x.updated_at
        self.x.save()
        self.assertNotEqual(self.x.updated_at, old_time)

    def test_new_amenity_dict(self):
        """
        Test if a new amenity can be created from a dictionary
        """
        self.x.name = "pool"
        dict_ = self.x.to_dict()
        self.y = Amenity(**dict_)
        self.assertEqual(self.x.name, self.y.name)

    def test_new_amenity_dict_attr_types(self):
        """
        Test if attributes of a new amenity created from a dictionary have correct types
        """
        self.x.name = "pool"
        dict_ = self.x.to_dict()
        self.y = Amenity(**dict_)
        for k, v in self.validAttributes.items():
            test_type = type(getattr(self.y, k))
            self.assertEqual(test_type, v)

    def test_save_user(self):
        """
        Test if storage saves the amenity correctly
        """
        self.assertIsInstance(self.storage._FileStorage__objects, dict)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file))
        self.assertTrue(os.stat(self.file).st_size != 0)

    def test_reload_amenity(self):
        """
        Test if storage reloads the amenity correctly
        """
        x_id = self.x.id
        x_id_key = "{}.{}".format(self.x.__class__.__name__, self.x.id)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertEqual(x_id,
                         self.storage._FileStorage__objects[x_id_key].id)

