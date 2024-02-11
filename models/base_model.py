#!/usr/bin/python3
"""
BaseModel Class definition
"""
import uuid
import copy
from datetime import datetime
import models


class BaseModel():
    """Defines the BaseModel Class"""

    valid_attributes = {
        "User": {
            'first_name': str,
            'last_name': str,
            'email': str,
            'password': str,
        }
    }

    def __init__(self, *args, **kwargs):
        # Initialize instance attributes
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self,
                            key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key == '__class__':
                    continue
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())  # Generate UUID
            self.created_at = datetime.now()  # Timestamp of creation
            self.updated_at = datetime.now()  # Timestamp of last update
            models.storage.new(self)

    def __str__(self):
        """String representation of an instance"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id,
                                      self.__dict__))

    def save(self):
        """Updates 'updated_at' attribute and saves instance"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance"""
        dict_ = copy.deepcopy(self.__dict__)
        dict_['updated_at'] = dict_['updated_at'].isoformat()
        dict_['created_at'] = dict_['created_at'].isoformat()
        dict_['__class__'] = self.__class__.__name__
        return dict_

