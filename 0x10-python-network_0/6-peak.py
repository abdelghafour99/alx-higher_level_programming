#!/usr/bin/python3
""" This function finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    else :
        return max(list_of_integers[0], find_peak(list_of_integers[1:]))
