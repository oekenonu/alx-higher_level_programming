#!/usr/bin/python3
"""Defines a class and inherits class checker."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj: object to be checked.
        a_class: The class to be checked against.
    Returns:
        True - If obj is an instance or inherits from a_class.
    """
    if isinstance(obj, a_class):
        return True
    return False
