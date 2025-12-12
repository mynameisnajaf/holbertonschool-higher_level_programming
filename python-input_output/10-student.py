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

    def to_json(self, attrs=None):
        """Function to give description of dict"""
        if attrs is None:
            return self.__dict__.copy()
        else:
            filtered={}
            for attr in attrs:
                if attr in self.__dict__:
                    filtered[attr] = self.__dict__[attr]
            return filtered
