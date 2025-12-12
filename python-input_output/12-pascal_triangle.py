#!/usr/bin/python3
"""Module that contains a function
   returns a list of lists of integers(Pascal)"""


def pascal_triangle(n):
    """returns a list of lists of integers(Pascal)"""
    triangle = []
    if n <= 0:
        return triangle
    else:
        for i in range(n):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        return triangle
