#!/usr/bin/python3
"""Class to define BaseModel for other classes"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """Class for all projects BaseModel"""

    def __init__(self, *args, **kwargs):
        """New base model initialization

        Args:
            *args (any): Not used.
            **kwargs (dict): Attr k/v pair.
        """

        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for k, val in kwargs.items():
                if "created_at" == k:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        date_format)
                elif "updated_at" == k:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        date_format)
                elif "__class__" == k:
                    pass
                else:
                    setattr(self, k, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Updated at current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dict of instance of BaseModels"""

        base_dict = self.__dict__.copy()
        base_dict["created_at"] = self.created_at.isoformat()
        base_dict["updated_at"] = self.updated_at.isoformat()
        base_dict["__class__"] = self.__class__.__name__

        return base_dict

    def __str__(self) -> str:
        """Str representation of base model instance"""
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def __repr__(self):
        """
        returns string repr
        """
        return (self.__str__())
