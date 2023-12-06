#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list and my_list[search]:
        nel = [replace for i in range(len(my_list))]
        for i in range(len(my_list)):
            if my_list[i] != search:
                nel[i] = my_list[i]
    return nel
