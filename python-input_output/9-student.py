#!/usr/bin/python3
"""Module that contains a function
   that returns the dict description"""


class Student:
    """Class that contains two functions"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Function to give description of dict"""
        return self.__dict__
