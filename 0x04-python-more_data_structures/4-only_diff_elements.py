#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = []
    if set_1 and set_2:
        for i in set_1:
            if i not in set_2:
                set_3.append(i)
        for i in set_2:
            if i not in set_1:
                set_3.append(i)
    elif set_1:
        set_3 = set_1
    elif set_2:
        set_3 = set_2
    return set_3
