#!/user/bin/python3
"""
Creating the parent class Base
"""

import uuid
import datetime


class BaseModel:
    """Base class"""

    def __init__(self, *args, **kwargs):
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
        dict_copy = {}
        dict_copy.update(self.__dict__)
        dict_copy["__class__"] = self.__class__
        dict_copy["update_at"] = str(datetime.datetime.isoformat(self.update_at))
        dict_copy["created_at"] = str(datetime.datetime.isoformat(self.created_at))
        dict_copy["id"] = str(self.id)
        return dict_copy
