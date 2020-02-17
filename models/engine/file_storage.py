#!/usr/bin/python3
"""
Filestorage funtion all, new, save, reload
"""
import json
import os.path
from models.base_model import BaseModel


class FileStorage():
    """ Init"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns dict """
        return type(self).__objects

    def new(self, obj):
        """ Sets new object in dictionary """
        if obj:
            self.__objects["{}.{}".format(
                obj.__class__.__name__, obj.id)] = obj

    def save(self):

    def reload(self):
