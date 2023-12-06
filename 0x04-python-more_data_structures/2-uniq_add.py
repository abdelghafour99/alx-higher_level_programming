#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = 0
    if my_list:
        for i in range(len(my_list)):
            if my_list[i] not in my_list[:i]:
                s += my_list[i]
    return s
