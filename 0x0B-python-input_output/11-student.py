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
         - If attrs is a list of strings,
           only attribute names contained in this list must be retrieved.
         - Otherwise, all attributes must be retrieved
         """

        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student
        """
        for i, j in json.items():
            setattr(self, i, j)
