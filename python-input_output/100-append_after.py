#!/usr/bin/python3
"""A module that contains
   a function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """A function that contains bla bla"""
    with open("{}".format(filename), "a", encoding="utf-8") as f:
        if search_string == new_string:
            return f.write(search_string)
