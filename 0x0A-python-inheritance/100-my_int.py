#!/usr/bin/python2
"""Defines class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operator == and !=."""

    def __eq__(self, value):
        """Override == opeartor to do the opposite"""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with its opposite"""
        return self.real == value
