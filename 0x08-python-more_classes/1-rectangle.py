#!/usr/bin/python3
""" Define a Rectangle class """


class Rectangle:
    """ Represents a rectangle """

    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ returns the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width of rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ return the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height of rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
