#!/usr/bin/python3
"""This module is for Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super.__init__(self, *args, **kwargs)
