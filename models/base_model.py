#!/usr/bin/python3
"""
Contains the class BaseModel that defines all common attributes/methods
"""
import models
import uuid
from datetime import datetime


class BaseModel():
    """
    Defines BaseModel as the base for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize BaseModel class

        Args:
            *args: Unused.
            **kwargs (dict): Key/value pairs of attributes.

        """
        if kwargs:
            if kwargs["__class__"] == self.__class__.__name__:
                self.id, self.created_at, self.updated_at, *_ = kwargs.values()
                self.created_at = datetime.strptime(
                        self.created_at, "%Y-%m-%dT%H:%M:%S.%f"
                        )
                self.updated_at = datetime.strptime(
                        self.updated_at, "%Y-%m-%dT%H:%M:%S.%f"
                        )
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        returns informal representation of an instance
        in the format [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the 'updated_at' attribute with the current date and time.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        """
        a key __class__ must be added to this dictionary
        with the class name of the object
        """
        dict_cp = self.__dict__.copy()
        dict_cp['__class__'] = self.__class__.__name__
        dict_cp['created_at'] = self.created_at.isoformat()
        dict_cp['updated_at'] = self.updated_at.isoformat()
        return dict_cp
