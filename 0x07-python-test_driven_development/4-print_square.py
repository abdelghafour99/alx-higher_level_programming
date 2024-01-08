#!/usr/bin/python3
"""
function that prints a square with the character #
"""


def print_square(size):
    """The code"""

    if type(size) != int or (type(size) == float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
