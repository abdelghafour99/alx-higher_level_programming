#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    p = 0
    i = 0
    while p < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            p += 1
            i += 1
        except (ValueError, TypeError):
            i += 1
        except IndexError:
            break
    print("")
    return(p)
