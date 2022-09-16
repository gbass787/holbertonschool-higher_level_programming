#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    prev = -1
    value = 0
    roman = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
            "D": 500, "M": 1000}
    for i in reversed(roman_string):
        for lttr, num in roman.items():
            if i == lttr:
                if prev <= num:
                    value += num
                else:
                    value -= num
                prev = num
    return value
