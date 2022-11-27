#!/usr/bin/python3
''' defines the BaseModel class '''
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    ''' this is a representation of the basemodel '''
    
    # instance - object of a class
    # attribute - variable / data
    # method - function in a class

    def __init__(self, *args, **kwargs):
        ''' constructor method '''

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        d_format = '%Y-%m-%dT%H:%M:%S.%f'

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(value, d_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        ''' return class name self id and self dict '''
        class_name = self.__class__.__name__
        return('[{:s}] ({:s}) {}'.format(class_name, self.id, self.__dict__))

    def save(self):
        ''' update the updated_at instance attribute '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        ''' return a dictionary containing all key/value of __dict__ '''
        b_model_dict = self.__dict__.copy()
        b_model_dict['__class__'] = self.__class__.__name__
        b_model_dict['updated_at'] = self.updated_at.isoformat()
        b_model_dict['created_at'] = self.created_at.isoformat()
        return(b_model_dict)
'''
=======
#!/usr/bin/pyhon3
"""
Parent class that will inherit
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes/methods
    """
    def __init__(self, *args, **kwargs):
        """initializes all attributes
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], f)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """returns class name, id and attribute dictionary
        """
        class_name = "[" + self.__class__.__name__ + "]"
        dct = {k: v for (k, v) in self.__dict__.items() if (not v) is False}
        return class_name + " (" + self.id + ") " + str(dct)

    def save(self):
        """updates last update time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """creates a new dictionary, adding a key and returning
        datetimes converted to strings
        """
        new_dict = {}

        for key, values in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                new_dict[key] = values.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not values:
                    pass
                else:
                    new_dict[key] = values
        new_dict['__class__'] = self.__class__.__name__

        return new_dict
>>>>>>> 79066938d69a38c2ed66b52e76fb484d673d749
'''
