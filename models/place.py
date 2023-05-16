#!/usr/bin/python3
"""This is the module for place"""
from models.base_model import BaseModel
class State(BaseModel):
    def __init__(self, city_id: str, user_id: str, name: str, description: str, number_rooms: int, number_bathrooms: int, max_guest: int, price_by_night: int, latitude: float, longitude: float, amenity_ids: list):
        """Instantiate the class"""
        """Inherit all methods and properties from its parent"""
        super().__init__()
        self.name = name
        self.city_id = city_id
        self.user_id = user_id
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.amenity_ids = amenity_ids