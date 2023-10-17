#!/usr/bin/python3
"""square module that inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inheriting from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Intilalize square

        Args:
            size (int): The size of the Square
            x (int): The x coordinate of the Square
            y (int): The y coordinate of the Square
            id (int): Id of the Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """Update values using *args or **kwargs

        Args:
            *args: List of arguments in the order id, size, x, y
            **kwargs: Keyword arguments representing attributes
        """
        attributes = ["id", "size", "x", "y"]

        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of a square"""
        return {
                "id": self.id, "size": self.width,
                "x": self.x, "y": self.y
                }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return (f"[Square] ({self.id}) {self.x}/{self.y} "
                f"- {self.width}")
