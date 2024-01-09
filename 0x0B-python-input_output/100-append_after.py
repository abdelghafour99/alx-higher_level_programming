#!/usr/bin/python3
"""function that inserts a line of text to a file
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """The Code"""

    tex = ""
    with open(filename) as f:
        for lin in f:
            tex += lin
            if search_string in lin:
                tex += new_string
    with open(filename, "w") as fi:
        fi.write(tex)
