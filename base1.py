#!/usr/bin/env python3
import uuid

class Base:
    """Base class for other models in Airbnb."""
    def __init__(self, id=None, **kwargs):
        if not id:
            self.id = uuid.uuid4().hex
        else:
            self.id = id

        for key, value in kwargs.items():
            self.__dict__[key] = value

    def __str__(self):
        return f"The id of the object is {self.id}"

personDict = {"name": "Philip", "field": "SE"}
base1 = Base(**personDict)
base2 = Base('Ola')

print(base1, base2)
print(base1.__dict__, base2.__dict__)
