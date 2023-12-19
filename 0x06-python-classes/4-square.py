#!/usr/bin/python3
class Square:
    pass

    @size.setter
    def __init__(self, size):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns current square area"""
        return self.__size**2

    def __init__(self, size=0):
        """Initialises the data"""
        self.size = size

    @property
    def size(self):
        """Getter method"""
        return self.__size
