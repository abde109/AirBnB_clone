#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """This is the BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return the string representation of the BaseModel."""
        class_name = self.__class__.__name__
        obj_id = self.id
        relevant_dict = {key: self.__dict__[key] for key in ['first_name', 'id', 'created_at', 'updated_at'] if key in self.__dict__}
        return "[{}] ({}) {}".format(class_name, obj_id, relevant_dict)

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel."""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
