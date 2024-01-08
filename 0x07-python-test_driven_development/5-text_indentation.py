#!/usr/bin/python3
"""
function that prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """The code"""
    if type(text) != str:
        raise TypeError("text must be a string")
    for a in text:
        print(a, end="")
        if a in (".", "?", ":"):
            print("\n")
