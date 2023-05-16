#!/usr/bin/python3
"""This is the module for review"""

class State:
    def __init__(self, place_id: str, user_id: str, text: str):
        """Instantiate the class"""
        self.place_id = place_id
        self.user_id = user_id
        self.text = text 