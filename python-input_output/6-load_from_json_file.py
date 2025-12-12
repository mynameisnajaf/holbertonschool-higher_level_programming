#!/usr/bin/python3
"""Module that contains a function
   to read from JSON file"""

import json


def load_from_json_file(filename):
    """Function to read object from json file"""
    with open("{}".format(filename), 'r') as json_file:
        my_obj = json.load(json_file)
