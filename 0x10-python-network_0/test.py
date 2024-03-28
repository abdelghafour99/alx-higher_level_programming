#!/usr/bin/python3
""" This function finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    list_len = len(list_of_integers)
    if list_len == 0:
        return None
    peak = find_peak_index(list_of_integers, 0, list_len - 1)
    return list_of_integers[peak]


""" find_peak_index """


def find_peak_index(list_li, list_0, list_ln):
    if list_0 >= list_ln:
        return list_0
    mi = ((list_ln - list_0) // 2) + list_0
    if list_li[mi] > list_li[mi + 1]:
        return find_peak_index(list_li, list_0, mi)
    else:
        return find_peak_index(list_li, mi + 1, list_ln)
