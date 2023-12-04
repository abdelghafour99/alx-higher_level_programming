#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list and idx >= 0 and idx < len(my_list):
        ne_l = [0 for i in range(len(my_lisit)-1)]
        b = 0
        for i in range(len(ne_l)):
            if i == idx:
                b = 1
            else:
                ne_l[i] = my_list[i + b]
        return ne_l
    else:
        return my_list
