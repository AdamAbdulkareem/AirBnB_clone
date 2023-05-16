#!/usr/bin/python3
"""This is the module for city"""
from models.base_model import BaseModel
class City(BaseModel):
    def __init__(self, state_id: str, name: str):
        """Instantiate the class"""
        """Inherit all methods and properties from its parent"""
        super().__init__()
        self.state_id = state_id
        self.name = name