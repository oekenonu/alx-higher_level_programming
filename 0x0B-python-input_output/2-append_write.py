#!/usr/bin/python3
""" append to a file """


def append_write(filename="", text=""):
    """ append to the end of a text file

    Args:
    filename - name of file to write to
    text - string to write
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
