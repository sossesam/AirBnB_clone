#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}


    def all(self):
        return type(self).__objects

    def new(self, obj):
        new_id = f"{type(obj).__name__}.{obj.id}"
        type(self).__objects[new_id] = obj
        #print(f"---------{type(self).__objects}")

    def save(self):
        new_dict = {}
        with open(type(self).__file_path, "w") as f:
            for keys, values in type(self).__objects.items():
                new_dict[keys] = values.to_dict()
            json.dump(new_dict, f)

    def reload(self):
        try:
            with open(type(self).__file_path, "r") as f:
                obj = json.load(f)
                for each_obj in obj.values():
                    class_name = str(each_obj["__class__"])
                    del each_obj["__class__"]
                    self.new(eval(class_name)(**each_obj))
        except FileNotFoundError:
            pass

