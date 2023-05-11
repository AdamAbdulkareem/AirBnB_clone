#!/usr/bin/python3

import uuid
import datetime


class BaseModel:
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

    def __str__(self):
        return f"{self.__class__.__name__} {self.id} {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()
    
    def to_dict(self):
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__
