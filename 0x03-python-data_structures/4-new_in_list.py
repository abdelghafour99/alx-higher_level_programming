#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list


def new_in_list(my_list, idx, element):
    new_list = replace_in_list(my_list, idx, new_element)
    return new_list
