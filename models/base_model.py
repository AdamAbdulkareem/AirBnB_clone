#!/usr/bin/python3

import uuid
from datetime import datetime
class BaseModel:
    def __init__(self, id, created_at, updated_at):
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    def __str__(self):
        return f"{self.__class__.__name__} {self.id} {self.__dict__}"