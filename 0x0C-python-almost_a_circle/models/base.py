#!usr/bin/python3
"""Module that manages id attributes."""
import json


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

    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
