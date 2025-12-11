#!/usr/bin/python3

"""
Module that provides a function to list attributes and methods of an object.
"""

def lookup(obj):
    """
    Returns a list of attributes and methods of an object.
    Args:
        obj: The object to inspect.
    Returns:
        list: A list of strings representing the attributes and methods of the object.
    """
    return list(dir(obj))
