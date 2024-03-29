#!/usr/bin/python3
"""
The Class Square
"""


class Square:
    """
    Define a Square Class
    """

    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
