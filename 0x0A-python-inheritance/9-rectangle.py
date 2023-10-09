#!/usr/bin/python3
"""Defines class Rectangle inheriting from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent class Rectangle that inherits BaseGeometry."""

    def __init__(self, width, height):
        """Intialize Rectangle.

        Args:
            width (int): Rectangle width.
            height (int): Rectangle height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area of rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns default Rectangle width and height properties."""
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
