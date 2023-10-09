#!/usr/bin/python3
"""Defines an inherited class checker."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj: The object to be checked.
        a_class: The class to checked against.
    Returns:
        True - If obj is an inherited instance of a_class.
        or False Otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
