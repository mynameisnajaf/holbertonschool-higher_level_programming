#!/usr/bin/python3
"""Module that contains
   function that returns the Py representation"""

import json


def from_json_string(my_str):
    """a function that returns the Python repr"""
    return json.load(my_str)
