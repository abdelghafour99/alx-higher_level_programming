#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    for a in text:
        print(a, end="")
        if a in (".", "?", ":"):
            print("\n")
