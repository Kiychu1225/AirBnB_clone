#!/usr/bin/python3
"""
Module for unittests for the Review class
"""
import unittest
import os
import models
from models.review import Review


class TestReviewCreation(unittest.TestCase):
    """Test class for instantiating Review instance"""

    def setUp(self):
        """
        Prepare the test environment
        """
        self.file = 'file.json'  # Define the path to the JSON file
        try:
            os.remove(self.file)
        except:
            pass
        self.x = Review()  # Create an instance of Review
        self.validAttributes = {
            'place_id': str,
            'user_id': str,
            'text': str
        }  # Dictionary of valid attributes and their types
        self.storage = models.storage  # Instance of FileStorage

    def tearDown(self):
        """
        Clean up the test environment
        """
        try:
            os.remove(self.file)
        except:
            pass

    def createReview(self):
        """
        Create a Review object with specific attributes for testing
        """
        self.ex = Review()
        self.ex.place_id = "23asdk"
        self.ex.user_id = "asdfoie"
        self.ex.text = "text"

    def test_has_correct_class_name(self):
        """
        Test if the class name is correct
        """
        self.assertEqual('Review', self.x.__class__.__name__)

    def test_empty_has_attrs(self):
        """
        Test if an empty Review has the required attributes
        """
        for k in self.validAttributes:
            self.assertTrue(hasattr(self.x, k))

    def test_empty_attrs_type(self):
        """
        Test if attributes of an empty Review have correct types
        """
        for k, v in self.validAttributes.items():
            test_type = type(getattr(self.x, k))
            self.assertEqual(test_type, v)

    def test_added_attrs(self):
        """
        Test if additional attributes can be added to a Review
        """
        self.createReview()
        self.assertEqual(self.ex.place_id, "23asdk")
        self.assertEqual(self.ex.user_id, "asdfoie")

    def test_check_custom_attrs(self):
        """
        Test if custom attributes can be added to a Review
        """
        self.x.custom_attr = "Test"
        self.assertEqual(self.x.custom_attr, "Test")
        self.assertIsInstance(self.x.custom_attr, str)

    def test_save_time_change(self):
        """
        Test if saving a Review changes its 'updated_at' time
        """
        old_time = self.x.updated_at
        self.x.save()
        self.assertNotEqual(self.x.updated_at, old_time)

    def test_new_dict(self):
        """
        Test if a new Review can be created from a dictionary
        """
        self.createReview()
        dict_ = self.ex.to_dict()
        self.y = Review(**dict_)
        self.assertEqual(self.ex.place_id, self.y.place_id)

    def test_new_dict_attr_types(self):
        """
        Test if attributes of a new Review created from a dictionary have correct types
        """
        self.createReview()
        dict_ = self.ex.to_dict()
        self.y = Review(**dict_)
        for k, v in self.validAttributes.items():
            test_type = type(getattr(self.y, k))
            self.assertEqual(test_type, v)

