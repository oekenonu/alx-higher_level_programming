#!/usr/bin/python3
"""Defines a class checker."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of the specified class.

    Args:
        obj: object to be checked.
        a_class: class to check obj against.
    Returns:
        True - If the obj is exactly an instance of a_class.
    """
    if type(obj) is a_class:
        return True
    return False
