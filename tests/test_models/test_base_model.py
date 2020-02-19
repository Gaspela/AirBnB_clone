#!/usr/bin/python3
"""
Test cases for BaseModel
"""


import unittest
import os
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):
    """This is to testing the base model class"""

    @classmethod
    def setUpClass(cls):
        """Setting for the test"""
        cls.base = BaseModel()
        cls.base.name = "KC"
        cls.base.num = 28

    @classmethod
    def teardown(cls):
        """When this finished this will tear it down"""
        del cls.base

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """Passing pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/base_model.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_save_BaseModel(self):
        """Testing if save works"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.update_at)

    def test_init_BaseModel(self):
        """Testing if the base is an type BaseModel"""
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_method_Basemodel(self):
        """Verify if BaseModel have methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))


if __name__ == "__main__":
    unittest.main()
