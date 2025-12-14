#!/usr/bin/python3
"""A module that contains
   a function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """A function that doesh smth"""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        new_lines.append(line)
        if search_string in line:
            new_lines.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
