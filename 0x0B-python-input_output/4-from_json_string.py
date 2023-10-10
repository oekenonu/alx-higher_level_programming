#!/usr/bin/python3
""" From json string to object """
import json


def from_json_string(mystr):
    """ Convert json back to string

    Args
    mystr - object to be converted
    """
    return json.loads(mystr)
