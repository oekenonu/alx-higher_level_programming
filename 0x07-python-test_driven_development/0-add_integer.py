#!/usr/bin/python3

""" Function to add 2 given integers """

def add_integer(a, b=98):
    """ 
    Returns the sum of two decimal numbers in binary digits.

        Parameters:
            a (int): An integer value
            b (int): Another integer value

        Returns:
            sum (integer): the sum of a and b
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
