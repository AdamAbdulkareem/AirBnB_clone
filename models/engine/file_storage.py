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

    # def save(self):
    #     json_object = {}

    #     for key in self.__objects:
    #         json_object[key] = self.__objects[key].to_dict()

    #     with open(self.__file_path, mode="w", encoding="UTF8") as json_file:
    #         json.dump(self.__objects, json_file)

    # def reload(self):
    #     try:
    #         with open(self.__file_path, mode="r", encoding="UTF8") as json_file:
    #             for key, value in json.load(json_file).items():
    #                 attribute_value = eval(value["__class__"])(**value)
    #                 self.__objects[key] = attribute_value

    #     except FileNotFoundError:
    #         pass

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        ''' create empty dictionary'''
        json_object = {}
        """ fill dictionary with elements __objects """
        for key in self.__objects:
            json_object[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(json_object, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                # jlo = json.load(f)
                for key, value in json.load(f).items():
                    attri_value = eval(value["__class__"])(**value)
                    self.__objects[key] = attri_value
        except FileNotFoundError:
            pass