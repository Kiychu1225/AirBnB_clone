#!/usr/bin/python3
"""
Module for unittests for the State class
"""
import unittest
import os
import models
from models.state import State


class TestStateCreation(unittest.TestCase):
    """Test class for instantiating State"""

    def setUp(self):
        """
        Set up test environment
        """
        self.file = 'file.json'  # Define the path to the JSON file
        try:
            os.remove(self.file)
        except:
            pass
        self.x = State()  # Create an instance of State
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

    def createState(self):
        """
        Create a State object with specific attributes for testing
        """
        self.ex = State()
        self.ex.name = "New York"

    def test_has_correct_class_name(self):
        """
        Test if the class name is correct
        """
        self.assertEqual('State', self.x.__class__.__name__)

    def test_empty_has_attrs(self):
        """
        Test if an empty State has the required attributes
        """
        for k in self.validAttributes:
            self.assertTrue(hasattr(self.x, k))

    def test_empty_attrs_type(self):
        """
        Test if attributes of an empty State have correct types
        """
        for k, v in self.validAttributes.items():
            test_type = type(getattr(self.x, k))
            self.assertEqual(test_type, v)

    def test_added_attrs(self):
        """
        Test if additional attributes can be added to a State
        """
        self.createState()
        self.assertEqual(self.ex.name, "New York")

    def test_check_custom_attrs(self):
        """
        Test if custom attributes can be added to a State
        """
        self.x.custom_attr = "Test"
        self.assertEqual(self.x.custom_attr, "Test")
        self.assertIsInstance(self.x.custom_attr, str)

    def test_save_time_change(self):
        """
        Test if saving a State changes its 'updated_at' time
        """
        old_time = self.x.updated_at
        self.x.save()
        self.assertNotEqual(self.x.updated_at, old_time)

    def test_new_dict(self):
        """
        Test if a new State can be created from a dictionary
        """
        self.createState()
        dict_ = self.ex.to_dict()
        self.y = State(**dict_)
        self.assertEqual(self.ex.name, self.y.name)

    def test_new_dict_attr_types(self):
        """
        Test if attributes of a new State created from a dictionary have correct types
        """
        self.createState()
        dict_ = self.ex.to_dict()
        self.y = State(**dict_)
        for k, v in self.validAttributes.items():
            test_type = type(getattr(self.y, k))
            self.assertEqual(test_type, v)

    def test_save(self):
        """
        Test if storage saves the State correctly
        """
        self.assertIsInstance(self.storage._FileStorage__objects, dict)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file))
        self.assertTrue(os.stat(self.file).st_size != 0)

    def test_reload(self):
        """
        Test if storage reloads the State correctly
        """
        x_id = self.x.id
        x_id_key = "{}.{}".format(self.x.__class__.__name__, self.x.id)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertEqual(x_id,
                         self.storage._FileStorage__objects[x_id_key].id)

