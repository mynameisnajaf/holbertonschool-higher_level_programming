#!/usr/bin/python3

"""Module that contains an error class"""


class BaseGeometry:
    """Contains a function to raise error"""
    def area(self):
        """Function that raises Exception"""
        raise Exception("area() is not implemented")
