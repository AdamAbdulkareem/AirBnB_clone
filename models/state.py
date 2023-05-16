#!/usr/bin/python3
"""This is the module for state"""
from models.base_model import BaseModel
class State(BaseModel):
    def __init__(self, name: str):
        """Instantiate the class"""
        """Inherit all methods and properties from its parent"""
        super().__init__()
        self.name = name