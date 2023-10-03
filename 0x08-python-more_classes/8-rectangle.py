#!/usr/bin/python3
""" Define a Rectangle class """


class Rectangle:
    """ Represents a rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ returns the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """ returns the representation of rectangle with dimension """
        if self.__width == 0 or self.__height == 0:
            return ("")
        return "\n".join([str(self.print_symbol) * self.__width
                         for _ in range(self.__height)])

    def __repr__(self):
        """ returns official repr """
        return "Rectangle({0}, {1})".format(self.__width, self.__height)

    def __del__(self):
        """ prints bye message on delete """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns biggest rectangle based on area

        Args:
            rect1 (Rectangle): the first rectangle object
            rect2 (Rectangle): the second rectangle object

        Raises:
            TypeError when either rect1 or rect2 are not Rectangles
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
