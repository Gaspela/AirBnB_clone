#!/usr/bin/python3
"""
Test cases for the console
"""


import unittest
import sys
import models
from unittest.mock import patch
from unittest.mock import create_autoespec
from io import StringIO
import pep8
import os
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """This is to test the console"""

    @classmethod
    def setUpClass(cls):
        """Setting for the test"""
        cls.consol = HBNBCommand()

    @classmethod
    def teardown(cls):
        """At the end of the test this will it down"""
        del cls.consol

    def tearDown(self):
        """Remove temporaly file - file.json created as a result"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_console(self):
        """Passing pep8 to the console file"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_emptyline(self):
        """Testing empty line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_quit(self):
        """Testing the quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("quit")
            self.assertEqual('', f.getvalue())

    def test_all(self):
        """Testing the all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all asdfghjkl")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all State")
            self.assertEqual("[]\n", f.getvalue())

    def test_create(self):
        '''
        Test that create works
        '''
        console = self.create()
        console.onecmd("create User")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))


if __name__ == "__main__":
    unittest.main()
