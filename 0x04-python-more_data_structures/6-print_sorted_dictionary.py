#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for idx, val in sorted(a_dictionary.items()):
        print("{}: {}".format(idx, val))
