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


    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
        list_objs (list): list of inherited instance of base
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as myfile:
            if list_objs is None:
                myfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                myfile.write(Base.to_json_string(list_dicts))
