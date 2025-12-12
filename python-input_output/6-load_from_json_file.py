#!/usr/bin/python3
"""Module that contains a function
   to read from JSON file"""

import json


def load_from_json_file(filename):
    """Function to read object from json file"""
    with open("{}".format(filename), 'r', encoding='utf-8') as json_file:
        return json.load(json_file)
