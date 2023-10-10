#!/usr/bin/python3
""" Read File  """


def read_file(filename=""):
    """ function to read file given """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
