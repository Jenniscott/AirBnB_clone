#!/usr/bin/python3

import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines all common attributes/methods for other classes."""
<<<<<<< HEAD
=======


>>>>>>> 7955dd2d5a69f66ed1e7a04649b7b36ceb2f277a
    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
<<<<<<< HEAD
        """Updates the updated_at attribute with the current datetime
        xsxxsxand saves the instance."""
=======
        """Updates the updated_at attribute."""
>>>>>>> 7955dd2d5a69f66ed1e7a04649b7b36ceb2f277a
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        dict_repr = self.__dict__.copy()
        dict_repr["__class__"] = self.__class__.__name__
        dict_repr["created_at"] = self.created_at.isoformat()
        dict_repr["updated_at"] = self.updated_at.isoformat()
        return dict_repr
