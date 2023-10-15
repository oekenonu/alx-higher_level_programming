#!usr/bin/python3
"""Module that manages id attributes."""


class Base:
    """Base class that manages all other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize the id of base

        Args:
        id (int): sets the id of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
