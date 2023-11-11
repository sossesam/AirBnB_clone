#!/usr/bin/python3

"""
The base_model is the base class other classes inherits
the id, date created and date updated information from
"""

import  models
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        #convert the kwargs dictionary to an object
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if any(kwargs):
            fmt = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, fmt)
                setattr(self, key, value)
        else:
            models.storage.new(self)


    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    
    def to_dict(self):
        
        dic = dict(**self.__dict__)
        dic['__class__'] = str(type(self).__name__)
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()

        return (dic)




