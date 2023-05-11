#!/usr/bin/python3
"""
This module defines all common attributes or methods for other classes
"""
import uuid
import datetime


class BaseModel:
    """Base Class"""

    def __init__(self):
        """Instantiate the attributes of an object."""
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

    def __str__(self):
        """Returns the object representation in a string format."""
        return f"{self.__class__.__name__} {self.id} {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at with the
        current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__


first_instance = BaseModel()
print(first_instance)