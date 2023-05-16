#!/usr/bin/python3
"""This is the module for amenity"""
from models.base_model import BaseModel
class Amenity(BaseModel):
    def __init__(self, name: str):
        """Instantiate the class"""
        """Inherit all methods and properties from its parent"""
        super().__init__()
        self.name = name