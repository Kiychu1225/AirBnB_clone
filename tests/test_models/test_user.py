#!/usr/bin/python3
"""
Module for unittests for the User class
"""
import unittest
import os
import json
import datetime
import models
from models.user import User
from models.base_model import BaseModel


class TestUserCreationEmpty(unittest.TestCase):
    """Test class for instantiating empty user"""

    def setUp(self):
        """
        Set up test environment
        """
        self.file = 'file.json'  # Define the path to the JSON file
        try:
            os.remove(self.file)
        except:
            pass
        self.x = User()  # Create an instance of User
        self.validAttributes = {
            'email': str,
            'password': str,
            'first_name': str,
            'last_name': str
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
        self.assertEqual('User', self.x.__class__.__name__)

    def test_empty_user_has_attrs(self):
        """
        Test if an empty User has the required attributes
        """
        for k in self.validAttributes:
            self.assertTrue(hasattr(self.x, k))

    def test_empyt_user_attrs_type(self):
        """
        Test if attributes of an empty User have correct types
        """
        for k, v in self.validAttributes.items():
            test_type = type(getattr(self.x, k))
            self.assertEqual(test_type, v)

    def test_user_added_attrs(self):
        """
        Test if additional attributes can be added to a User
        """
        self.x.first_name = "Betty"
        self.x.last_name = "Betty"
        self.x.email = "airbnb@mail.com"
        self.x.password = "root"
        self.assertEqual(self.x.first_name, "Betty")
        self.assertEqual(self.x.last_name, "Betty")
        self.assertEqual(self.x.email, "airbnb@mail.com")
        self.assertEqual(self.x.password, "root")

    def test_check_custom_attrs(self):
        """
        Test if custom attributes can be added to a User
        """
        self.x.custom_attr = "Test"
        self.assertEqual(self.x.custom_attr, "Test")
        self.assertIsInstance(self.x.custom_attr, str)

    # TODO: This fails occasionally
    def test_save_time_change(self):
        """
        Test if saving a User changes its 'updated_at' time
        """
        old_time = self.x.updated_at
        self.x.save()
        self.assertNotEqual(self.x.updated_at, old_time)

    def test_new_user_dict(self):
        """
        Test if a new User can be created from a dictionary
        """
        self.x.first_name = "Betty"
        self.x.last_name = "Betty"
        self.x.email = "airbnb@mail.com"
        self.x.password = "root"
        dict_ = self.x.to_dict()
        self.y = User(**dict_)
        self.assertEqual(self.x.first_name, self.y.first_name)
        self.assertEqual(self.x.last_name, self.y.last_name)
        self.assertEqual(self.x.email, self.y.email)
        self.assertEqual(self.x.password, self.y.password)

    def test_new_user_dict_attr_types(self):
        """
        Test if attributes of a new User created from a dictionary have correct types
        """
        self.x.first_name = "Betty"
        self.x.last_name = "Betty"
        self.x.email = "airbnb@mail.com"
        self.x.password = "root"
        dict_ = self.x.to_dict()
        self.y = User(**dict_)
        for k, v in self.validAttributes.items():
            test_type = type(getattr(self.y, k))
            self.assertEqual(test_type, v)

    def test_save_user(self):
        """
        Test if storage saves the User correctly
        """
        self.assertIsInstance(self.storage._FileStorage__objects, dict)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file))
        self.assertTrue(os.stat(self.file).st_size != 0)

    def test_reload_user(self):
        """
        Test if storage reloads the User correctly
        """
        x_id = self.x.id
        x_id_key = "{}.{}".format(self.x.__class__.__name__, self.x.id)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertEqual(x_id,
                         self.storage._FileStorage__objects[x_id_key].id)


class TestUserCreation(unittest.TestCase):
    """Test class for User class instantiation tests"""

    def setUp(self):
        """
        Set up test environment
        """
        self.file = 'file.json'  # Define the path to the JSON file
        try:
            os.remove(self.file)
        except:
            pass
        self.x = User()  # Create an instance of User
        self.x.first_name = "Betty"
        self.x.last_name = "Betty"
        self.x.email = "airbnb@mail.com"
        self.x.password = "root"
        self.x.save()  # Save the User instance
        self.fp = open('file.json', 'r', encoding="utf-8")  # Open the JSON file
        self.dict_ = json.load(self.fp)  # Load the content of the JSON file
        self.validAttributes = {
            'email': str,
            'password': str,
            'first_name': str,
            'last_name': str
            }  # Dictionary of valid attributes and their types

    def tearDown(self):
        """
        Clean up test environment
        """
        try:
            self.fp.close()  # Close the JSON file
        except:
            pass
        try:
            os.remove(self.file)  # Remove the JSON file
        except:
            pass

    def test_test_all_attrs(self):
        """
        Test if all attributes have correct types
        """
        for k, v in self.validAttributes.items():
            test_attr = getattr(self.x, k)
            self.assertIsInstance(test_attr, v)

    def test_user_creation(self):
        """
        Test if User instance is created correctly
        """
        self.assertIsInstance(self.x, BaseModel)
        self.assertIsInstance(self.x, User)

    def test_is_classname(self):
        """
        Test if the class name is correct

