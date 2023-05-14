"""This module create a file storage that is used to save objects"""
import json


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
        """serializes __objects to the JSON file (path: __file_path)"""

        """ create empty dictionary"""
        json_object = {}

        for key in self.__objects:
            json_object[key] = self.__objects[key].to_dict()


        with open(self.__file_path, mode="w", encoding="UTF8") as json_file:
            json.dump(self.__objects, json_file)
