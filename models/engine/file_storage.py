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
        return self.__objects

    # def new(self, obj):
    #     self.__objects["__class__.__name__.id"] = obj

    def save(self):
        with open(self.__file_path, "w") as json_file:
            json.dump(self.__objects, json_file)
        json_file.close()
    
    def reload(self):
        if self.__file_path:
            with open(self.__file_path, "r") as json_file:
                self.__objects = json.loads(json_file)
        else:
            return
# first_instance = FileStorage()
# print(first_instance.file_path)
# first_instance.save()
# print(first_instance.save())