#!/usr/bin/python3
""" Save a json object to file """
import json


def save_to_json_file(myobj, filename):
    """ Convert object passed to json representation
        and save to file

    Args
    myobj - object to be converted
    filename - name of file to write to
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(myobj))
