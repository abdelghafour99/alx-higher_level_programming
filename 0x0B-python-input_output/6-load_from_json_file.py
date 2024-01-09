#!/usr/bin/python3
"""
function that load an Object to a text file, using a JSON representation
"""


import json


def load_from_json_file(filename):
    """The code"""

    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
