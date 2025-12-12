#!/usr/bin/python3

"""Module that contains a function
   to write to file and return number of chars"""


def append_write(filename="", text=""):
    """Function to write to a file"""
    with open("{}".format(filename), 'a', encoding="utf-8") as f:
        return f.write("{}".format(text))
