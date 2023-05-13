#!/usr/bin/python3
"""
This module defines all common attributes or methods for other classes
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Base Class"""

    def __init__(self, *args, **kwargs):
        """Instantiate the attributes of an object."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().isoformat()
            self.updated_at = datetime.now().isoformat()
            storage.new(self)

    def __str__(self):
        """Returns the object representation in a string format."""
        return f"{self.__class__.__name__} {self.id} {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at with the
        current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__
