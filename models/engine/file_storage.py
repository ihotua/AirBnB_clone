#!/usr/bin/python3
"""
This script defines the class FileStorage.
"""
import json
import uuid
import os
from models.base_model import BaseModel
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """ The construct """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary objects"""
        return (FileStorage.__objects)

    def new(self, obj):
        """Sets in dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes objects to the JSON file """
        json_objects = {key: obj.to_dict() for key,
                obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """ Reload file """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                json_objects = json.load(f)
                for key, obj_dict in json_objects.items():
                    cls_name = obj_dict['__class__']
                    cls = globals().get(cls_name)
                    if cls:
                        obj = cls(**obj_dict)
                        FileStorage.__objects[key] = obj
