#!/usr/bin/python3
"""
My class student
"""


class Student:
    """The class Student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student"""
        self.__name = name
        self.number = number
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance:
         - If attrs is a list of strings,
           only attribute names contained in this list must be retrieved.
         - Otherwise, all attributes must be retrieved
         """

        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__
