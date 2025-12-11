#!/usr/bin/python3

"""Module that contains a function to check isinstance"""


def is_kind_of_class(obj, a_class):
    """Function to check obj is an instance of the specified class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
