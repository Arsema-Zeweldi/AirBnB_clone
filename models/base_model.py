#!/usr/bin/python3

"""
a module that implements the BaseModel class
"""

import uuid
from datetime import datetime 
import models 
from models import storage 


class BaseModel:
    
    """
    BaseModel - A class that defines all common attributes/methods for other classes
    """
    def __init__(self,*args, **kwargs):
        """
        Initialize the BaseModel class
        """
        
        from models import storage 
        if not kwargs:
            self.id=str(uuid.uuid4)
            self.created_at=datetime.now()
            self.updated_at=datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__' :
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self,key, value)
    def __str__(self):
        """
        Returns the string representation of BaseModel Object
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)
    
    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        from models import storage
        
        self.updated_at=datetime.now()
        storage.save()
        
    def to_dict(self):
        """
        - returns a dictionary containing all keys/values of __dict__ of the instance
        
        - by using self.__dict__, only instance attributes set will be returned
        - a key __class__ must be added to this dictionary with the class name of the object
        - created_at and updated_at must be converted to string object in ISO format
        """
        d = self.__dict__.copy()
        d["__class__"]=self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ("created_at", "updated_at"):
                v = self.__dict__[k].isoformat()
                d[k] = v
        return d
         
         
