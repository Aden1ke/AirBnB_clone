#!/usr/bin/python3
"""
File Storage Module
This module is in charge of the storage of the classes
"""
import json
from models.base_model import BaseModel
from models.user import User
from os import path



class FileStorage:
    """
    This class that serialize and deserialize instances of models
    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary to store the instances
            by their class name and id.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieves all objects stored in the __objects dicti
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the __objects dictionary.

        Args:
            obj: The object instance to be added.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes the objects stored in the __objects dictionary
        """
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the objects from the JSON file and stores
        them in the __objects dictionary.
        """
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj = globals()[class_name](**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
