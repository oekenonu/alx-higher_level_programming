#!/usr/bin/python3
""" Creates a json object """
import json


def to_json_string(myobj):
    """ Convert object passed to json representation

    Args
    myobj - object to be converted
    """
    return json.dumps(myobj)
