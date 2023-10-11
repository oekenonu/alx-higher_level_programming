#!/usr/bin/python3
""" Show dictionary description for json obj """


def class_to_json(obj):
    """ returns disctionary description

    Args:
    obj - instance of a class
    """
    return obj.__dict__
