#!/usr/bin/python3

"""Module that contains an error class"""


class BaseGeometry:
    """Contains a function to raise error"""
    def area(self):
        """Function that raises Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A function that validates value"""
        if not isinstance(value, int):
            raise TypeError("name must be an integer")
        if value <= 0:
            raise ValueError("name must be greater than 0")
