#!/usr/bin/python3

""" Defines a locked class """


class LockedClass:
    """ prevents the user from dynamically creating new instance attributes """
    def __setattr__(self, attr, value):
        if hasattr(self, attr):
            raise AttributeError("'LockedClass' object attribute '{}'
                                 is read-only".format(attr))
        elif attr == 'first_name':
            super().__setattr__(attr, value)
        else:
            raise AttributeError("'LockedClass' object has no
                                 attribute '{}'".format(attr))
