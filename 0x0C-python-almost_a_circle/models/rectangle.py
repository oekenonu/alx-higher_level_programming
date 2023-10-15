#!/usr/bin/python3
"""Module that uses the Base class"""
from models.base import Base 


class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize Rectangle

        Args:
        width (float/int): the width of the rectangle
        height (float/int): the height of the rectangle
        x (int): x coordinate
        y (int): y coordinate
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return __width
    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return __height
    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return __y
    @y.setter
    def y(self, y):
        self.__y = y
