#!/usr/bin/python3
def roman_to_int(roman_string):
    my_list = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    S = 0
    for i in range(len(roman_string)):
        if roman_string[i] not in my_list:
            return 0
        a = my_list[roman_string[i]]
        c = 1
        if i < len(roman_string) - 1:
            b = my_list[roman_string[i + 1]]
            if a < b:
                S -= a
                c = 0
        if c:
            S += a
    return S
