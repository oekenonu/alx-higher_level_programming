#!/usr/bin/python3
"""Defines Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square which inherits from Rectangle."""

    def __init__(self, size):
        """Initialize square.

        Args:
            size (int): square size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
