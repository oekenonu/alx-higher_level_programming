#!/usr/bin/python3
""" Define class MyList that inherits from list """


class MyList(list):
    """ Uses the sorted func from list class """

    def print_sorted(self):
        """Print a list sorted in ascending order."""
        print(sorted(self))
