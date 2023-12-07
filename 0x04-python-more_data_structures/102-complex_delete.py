#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    return {k: v if v != value else None for k, v in a_dictionary.items()}
