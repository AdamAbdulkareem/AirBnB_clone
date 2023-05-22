#!/usr/bin/python3
"""This is the module for review"""
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
