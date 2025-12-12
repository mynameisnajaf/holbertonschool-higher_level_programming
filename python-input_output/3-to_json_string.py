#!/usr/bin/python3
"""Module that contains
   function that returns the JSON representation"""

import json


def to_json_string(my_obj):
    """a function that returns the JSON repr"""
    return json.dumps(my_obj)
