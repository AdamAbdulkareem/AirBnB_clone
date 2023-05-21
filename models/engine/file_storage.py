"""This module convert the dictionary representation to a JSON string"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """Serializes instances to a JSON file and Deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes objectss to the JSON file (path: __file_path) """
        json_object = {}

        for key, value in self.__objects.items():
            json_object[key] = value.to_dict()

        with open(self.__file_path, mode="w", encoding="UTF8") as json_file:
            json.dump(json_object, json_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding="UTF8") as f:
                for key, value in json.load(f).items():
                    class_name = value.get("__class__")
                    if class_name == "User":
                        obj = User(**value)
                        self.__objects[key] = obj

                    if class_name == "Amenity":
                        obj = Amenity(**value)
                        self.__objects[key] = obj

                    if class_name == "City":
                        obj = City(**value)
                        self.__objects[key] = obj
                        
                    if class_name == "Place":
                        obj = Place(**value)
                        self.__objects[key] = obj
                        
                    if class_name == "Review":
                        obj = Review(**value)
                        self.__objects[key] = obj
                        
                    if class_name == "State":
                        obj = User(**value)
                        self.__objects[key] = obj
                        
                    if class_name == "State":
                        obj = State(**value)
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass
