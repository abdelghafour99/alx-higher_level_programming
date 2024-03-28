#!/usr/bin/python3
''' This function finds a peak in a list of unsorted integers '''


def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    return max(list_of_integers[0], find_peak(list_of_integers[1:]))
