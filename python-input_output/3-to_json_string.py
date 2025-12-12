#!/usr/bin/python3
import json
"""Module that contains
   function that returns the JSON representation"""



def to_json_string(my_obj):
    """a function that returns the JSON repr"""
    return json.dumps(my_obj)
