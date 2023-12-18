#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    p = 0
    while p < x:
        try:
            print(my_list[p], end="")
            p += 1
        except Exception:
            break
    print("")
    return(p)
