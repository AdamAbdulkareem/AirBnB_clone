#!/usr/bin/python3
"""This module is for City"""
from models.base_model import BaseModel


class City(BaseModel):
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super.__init__(self, *args, **kwargs)
