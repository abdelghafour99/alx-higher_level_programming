#!/usr/bin/python3
"""
function that writes a text file (UTF8) and prints it to stdout
"""


def write_file(filename=""):
    with open(filename, "w", encoding="utf-8") as f:
        read_data = f.read
        print(read_data, end="")
        return(len(list(f)))
