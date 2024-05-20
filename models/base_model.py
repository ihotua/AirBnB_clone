#!/usr/bin/python3
"""This defnes the BaseModel Class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        This initializes the base model attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime
                    (value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        This returns the string representation
        """
        ihname = self.__class__.__name__
        return "[{}] ({}) {}".format(ihname, self.id, self.__dict__)

    def save(self):
        """
        It updates the attribute with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        A dictionary containing all attributes and their values
        """
        ih_diction = self.__dict__.copy()
        ih_diction["__class__"] = self.__class__.__name__
        ih_diction["created_at"] = self.created_at.isoformat()
        ih_diction["updated_at"] = self.updated_at.isoformat()
        return (ih_diction)
