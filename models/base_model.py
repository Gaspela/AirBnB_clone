#!/user/bin/python3
"""
Creating the parent class Base
"""


import uuid
import datetime


class BaseModel:
    """Base class"""

    def __init__(self, id=None, created_at=None, update_at=None):
        """Class constructor"""

        if id is not None:
            self.id = id

        """Init method"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.update_at = datetime.datetime.now()

    def __str__(self):
        """Object string representation"""
        return "[<{}>] (<{}>) <{}>".format("BaseModel", self.id, self.__dict__)

    def save(self):
        """Update public instance attr up"""
        self.update_at = datetime.datetime.now()

    def to_dict(self):
        """Return dict"""
        self.update_at = str(datetime.datetime.isoformat(self.update_at))
        self.created_at = str(datetime.datetime.isoformat(self.created_at))

        dict_copy = self.__dict__
        d = {self.__class__: self}
        d.update(dict_copy)
        return dict_copy
