#!/usr/bin/python3

"""
The base_model is the base class other classes inherits
the id, date created and date updated information from
"""

import uuid
from datetime import datetime as dt

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = dt.now()
        self.updated_at = dt.now()

    def __str__(self):
        return f"[{type(self).__name__}] {self.id} {self.__dict__}"

    def save(self):
        self.updated_at = dt.now()
    
    def to_dict(self):
        dict = {}
        for key, values in self.__dict__.items():
            dict[key] = values
            if (key == "created_at") or (key == "updated_at"):
                dict[key] = values.isoformat()

        dict["__class__"]= type(self).__name__

        return dict




