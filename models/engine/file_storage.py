#!/usr/bin/python3
''' define a FileStorage class '''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    ''' serializes instances to a JSON file and deserialize

    Attributes:
    __file_path (str): path to JSON file save as
    __objects (dictionary): a dict of instanciated objects
    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' returns the dictionary '''
        return (FileStorage.__objects)

    def new(self, obj):
        ''' set in __objects the obj with key <obj class name>.id '''
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class_name, obj.id)] = obj

    def save(self):
        ''' serializes __objects to the JSON file(path: __file_path) '''
        obj_dict = FileStorage.__objects
        obj_dict_ = {obj: obj_dict[obj].to_dict() for obj in obj_dict.keys()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict_, f)

    def reload(self):
        ''' deserialize the JSON file __file_path to __objects, if it exits '''
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict_ = json.load(f)
                for o in obj_dict_.values():
                    obj_class_name = o['__class__']
                    del o['__class__']
                    self.new(eval(obj_class_name)(**o))
        except FileNotFoundError:
            return
