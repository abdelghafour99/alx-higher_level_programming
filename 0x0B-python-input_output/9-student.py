#!/usr/bin/python3
"""
My class student
"""


class Student:
    """The class Student"""

    def __init__(self, first_name, last_name, age):
        self.__name = name
        self.number = number
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance."""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
