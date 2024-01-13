#!/usr/bin/python3
"""
The Square Class
"""


class Square:
    """
    Define a Square Class
    """

    @size.setter
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size**2

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size
