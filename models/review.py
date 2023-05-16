#!/usr/bin/python3
"""This is the module for review"""
from models.base_model import BaseModel
class State(BaseModel):
    def __init__(self, place_id: str, user_id: str, text: str):
        """Instantiate the class"""
        """Inherit all methods and properties from its parent"""
        super().__init__()
        self.place_id = place_id
        self.user_id = user_id
        self.text = text 