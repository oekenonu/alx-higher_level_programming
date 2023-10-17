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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y mut be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """print out the rectangle instance with # character"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(' ',end='')
            for _ in range(self.__width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        """update values
        - 1st argument represents id attribute
        - 2nd argument represents width attribute
        - 3rd argument represent height attribute
        - 4th argument represents x attribute
        - 5th argument represents y attribute
        """
        attributes = ["id", "width", "height", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """dictionary representation function"""
        return {
                "id": self.id, "width": self.width,
                "height": self.height, "x": self.x,
                "y": self.y
                }

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} "
                "- {self.__width}/{self.__height}")
