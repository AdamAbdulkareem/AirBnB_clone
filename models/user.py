#!/usr/bin/python3
"""This is the module for user"""
from models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, email: str, password: str, first_name: str, last_name: str):
        """Instantiate the class"""
        """Inherit all methods and properties from its parent"""
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name