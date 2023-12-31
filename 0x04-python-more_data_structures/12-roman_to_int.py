#!/usr/bin/python3
def roman_to_int(roman_string):
    my_list = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    S = 0
    if roman_string and isinstance(roman_string, str):
        for i in range(len(roman_string)):
            if roman_string[i] not in my_list:
                return 0
            a = my_list[roman_string[i]]
            if i < len(roman_string) - 1:
                b = my_list[roman_string[i + 1]]
                if a < b:
                    S -= 2 * a
            S += a
    return S
