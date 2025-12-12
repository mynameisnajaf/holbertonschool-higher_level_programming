#!/usr/bin/python3
"""Module that contains a function
   that returns the dict description"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object
    for JSON serialization.
    """
    return obj.__dict__
