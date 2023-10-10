#!/usr/bin/python3
""" From json file to tring object """
import json


def load_from_json_file(filename):
    """ Read json file to string

    Args
    filename - name of file to read
    """
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
