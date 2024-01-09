#!/usr/bin/python3
"""
function that load an Object to a text file, using a JSON representation
"""


import json


def load_to_json_file(my_obj, filename):
    """The code"""

    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
