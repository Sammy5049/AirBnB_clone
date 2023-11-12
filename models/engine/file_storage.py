#!/usr/bin/python3

"""Storage for all file storage class"""

from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.city import City
from models.base_model import BaseModel
import json


class FileStorage:
    """Rep the file storage

    Attributes:
        __file_path (str): path to safe the obj to.
        __objects: dictionary of instance of an object
        class_dict (dict): A dictionary of all the classes.
    """

    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

    def all(self):
        """Returns __objects dictionary"""
        return self.__objects

    def new(self, obj):
        '''Set new __objects to existing dictionary of instances'''
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serialization of __objects to JSON file in file.json path"""

        obj_dict = {}

        for k, obj in self.__objects.items():
            obj_dict[k] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="UTF-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """"Deserialization of the json file back to object if exists"""

        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)

                for k, val in obj_dict.items():
                    obj = self.class_dict[val['__class__']](**val)
                    self.__objects[k] = obj
        except FileNotFoundError:
            return
