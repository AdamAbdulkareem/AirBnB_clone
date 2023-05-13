#!/usr/bin/python3
"""
This module converts the dictionary representation to a JSON string
"""
import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances"""

    def __init__(self, file_path: str):
        """Instantiate the attributes of an object."""
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __object the obj with the key <obj class name>.id"""
        self.__objects = f"{obj.__class__.__name__}.{obj.id}"

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, "w") as json_file:
            json.dump(self.__objects, json_file)
        json_file.close()

    def reload(self):
        """Deserializes the JSON file"""
        if self.__file_path:
            with open(self.__file_path, "r") as json_file:
                self.__objects = json.loads(json_file)
        else:
            return
