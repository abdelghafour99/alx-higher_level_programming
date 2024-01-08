#!/usr/bin/python3
"""
function that prints a square with the character #
"""


def say_my_name(first_name, last_name=""):
    """The code"""
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
