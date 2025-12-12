#!/usr/bin/python3

"""Module that contains a function
   to read file and print it"""


def read_file(filename=""):
    """Function to read and print file"""
    with open("{}".format(filename), encoding="utf-8") as f:
       print(f.read(), end="")
