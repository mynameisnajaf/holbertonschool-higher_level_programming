#!/usr/bin/python3

"""
Module that provides a function to that prints the list, but sorted (ascending sort).
"""


class MyList(list):
    """
    Class that contains function that prints sorted list
    """
    def print_sorted(self):
        """Prints sorted list"""
        print(sorted(self))
