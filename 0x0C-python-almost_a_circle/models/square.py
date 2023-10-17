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
            id (int): Identity of the Square
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


    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return (f"[Square] ({self.id}) {self.x}/{self.y} "
                f"- {self.width}")
