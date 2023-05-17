#!/usr/bin/python3
"""This module is for Amenity"""
from models.base_model import BaseModel


class State(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super.__init__(self, *args, **kwargs)
