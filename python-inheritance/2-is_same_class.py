#!/usr/bin/python3

"""Module that contains a function to check isinstance"""


def is_same_class(obj, a_class):
    """Function to check obj is an instance of the specified class"""
    if type(obj) is a_class:
        return True
    else:
        return False
