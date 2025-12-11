#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Represent a square using Rectangle."""

    def __init__(self, size):
        """Intialize a new Square.

        Args:
            size (int): The size of the new Square.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of a square"""
        return self.__size*self.__size
