#!/usr/bin/python3
""" BaseModel class """


import uuid
from datetime import datetime
import models
from json import JSONEncoder


class BaseModel:
    """BaseModel"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        class_name = self.__class__.__name__
        return("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dict_repr = {}
        for key, value in self.__dict__.items():
            dict_repr[key] = value
            if isinstance(value, datetime):
                dict_repr[key] = value.strftime('%Y-%m-%dT%H:%M:%S.%f')
        dict_repr["__class__"] = type(self).__name__
        return dict_repr


class BaseModelEncoder(JSONEncoder):
    """JSON"""
    def default(self, o):
        if isinstance(o, BaseModel):
            return o.to_dict()
        return super().default(o)
