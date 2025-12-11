#!/usr/bin/python3

"""Module that contains a function to check isinstance"""


def inherits_from(obj, a_class):
    """Function to check obj is an instance of the specified class
    that inherited (directly or indirectly) from the specified class"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
