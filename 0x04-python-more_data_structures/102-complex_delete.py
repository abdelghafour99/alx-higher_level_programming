#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i in list(a_dictionary):
        if a_dictonary[i] == value:
            del a_dictionary[i]
    return a_dictionary[i]
#{k: v if v != value else None for k, v in a_dictionary.items()}
