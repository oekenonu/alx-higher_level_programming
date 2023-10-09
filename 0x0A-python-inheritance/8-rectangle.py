#!/usr/bin/python3
"""Defines class Rectangle which inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle class inheriting BaseGeometry."""

    def __init__(self, width, height):
        """Intialize Rectangle.

        Args:
            width (int): Width of Rectangle.
            height (int): Height of Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
