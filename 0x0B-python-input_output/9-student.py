#!/usr/bin/python3
"""My class Student"""


class Student:
    """The Class student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance:
        """

        return self.__dict__
