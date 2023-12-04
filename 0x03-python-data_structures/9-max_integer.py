#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        b = my_list[0]
        for a in my_list:
            if a > b:
                b = a
        return b
    else:
        return None
