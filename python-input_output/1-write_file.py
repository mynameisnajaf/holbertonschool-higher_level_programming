#!/usr/bin/python3

"""Module that contains a function
   to write to file and return number of chars"""


def write_file(filename="", text=""):
    """Function to read and print file"""
    with open("{}".format(filename), 'w', encoding="utf-8") as f:
        return f.write("{}".format(text))
