#!/usr/bin/python3
""" BaseModel class """


import uuid
from datetime import datetime
import models
from json import JSONEncoder


class BaseModel:
    """BaseModel"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(
                            value,
                            '%Y-%m-%dT%H:%M:%S.%f')
                if key not in ['__class__']:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """ save method """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ to_dict method """
        dict_repr = self.__dict__.copy()
        dict_repr["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                value = self.__dict__[key].isoformat()
                dict_repr[key] = value
        return dict_repr

    def __str__(self):
        """ __str__ method """
        class_name = self.__class__.__name__
        return("[{}] ({}) {}".format(class_name, self.id, self.__dict__))


class BaseModelEncoder(JSONEncoder):
    """JSON"""
    def default(self, o):
        if isinstance(o, BaseModel):
            return o.to_dict()
        return super().default(o)
