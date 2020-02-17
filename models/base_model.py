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
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Update with self.updated and time.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return __dict__ value, key.
        Convert Str to iso format.
        serialization and deserialization.
        """

        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
