#!/usr/bin/python3
"""
function that appends a string at the end of a text file (UTF8) and returns the number of characters added
"""


def write_file(filename="", text=""):
    """The code"""

    with open(filename, "a", encoding="utf-8") as f:
        alen = f.write(text)
        return(alen)
