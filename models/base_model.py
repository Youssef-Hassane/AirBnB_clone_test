#!/usr/bin/python3
"""
Base class providing common functionality for other models.
Contains an id, created and updated time.
"""
from uuid import uuid4 as UNIQUE_ID
from datetime import datetime as TIME


class BaseModel():
    """
    Base model for other models to inherit from.
    Provides basic functionality such as ID, created and updated times.
    """

    def __init__(self, *args, **kwargs):
        """	Initialise model """
        self.id = str(UNIQUE_ID())
        self.created_at = TIME.now()
        self.updated_at = TIME.now()

    def __str__(self):
        """	Return string representation of model """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """	Save model changes """
        self.updated_at = TIME.now()

    def to_dict(self):
        """	Convert model to dictionary """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
