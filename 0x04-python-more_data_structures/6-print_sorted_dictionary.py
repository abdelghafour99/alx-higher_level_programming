#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_list = sorted(list(a_dictionary))
    if my_list:
        for a in my_list:
            print("{} : {}".format(a, a_dictionary[a]))