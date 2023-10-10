#!/usr/bin/python3
""" writes to a file """


def write_file(filename="", text=""):
    """ write a string to a text file

    Args:
    filename - name of file to write to
    text - string to write
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
