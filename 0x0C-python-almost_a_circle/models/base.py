#!/usr/bin/python3
"""
Base Class
"""

class Base:
    """
    Define a new Class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        self.__id = id
        if id != None:

        else:
            __nb_objects += 1

