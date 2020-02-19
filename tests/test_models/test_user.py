#!/usr/bin/python3
"""
Tesst cases for user
"""


import unittest
import os
from models.user import User
from models.base_model import BaseModel
import pep8


class TestUser(unittest.TestCase):
    """This will test the user class"""

    @classmethod
    def setUpClass(cls):
        """Setting for the test"""
        cls.user = User()
        cls.user.first_name = "Kevin"
        cls.user.last_name = "Caspin"
        cls.user.email = "1169@holbertonschool.com"
        cls.user.password = "secret"

    @classmethod
    def teardown(cls):
        """Killing at the end of the test"""
        del cls.user

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_User(self):
        """Testing pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_attributes_User(self):
        """Chekcing if User have attributes"""
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_is_subclass_User(self):
        """Testing if User is subclass of BaseModel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_save_User(self):
        """Test if the save works"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict_User(self):
        """Test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.user), True)


if __name__ == "__main__":
    unittest.main()
