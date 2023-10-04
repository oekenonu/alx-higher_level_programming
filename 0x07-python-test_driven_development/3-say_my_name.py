#!/usr/bin/python3
'''
This module introduces the fullnames of persons
'''


def say_my_name(first_name, last_name=""):
    '''
    returns fullname from first_name and last_name

    Args:
    first_name (str): the firstname
    last_name (str): the lastname

    Raises:
    TypeError: if argument passed is not of type str

    Returns:
    (str): concatenated first_name and last_name with additional text
    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
