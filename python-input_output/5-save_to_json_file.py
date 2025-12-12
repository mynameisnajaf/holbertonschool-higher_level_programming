#!/usr/bin/python3
"""Module that contains a function
   to save to JSON file"""

import json


def save_to_json_file(my_obj, filename):
    """Function to save object to json file"""
    with open("{}".format(filename), 'w') as json_file:
        json.dump(my_obj, json_file)
