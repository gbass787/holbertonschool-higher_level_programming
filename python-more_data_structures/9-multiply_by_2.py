#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for i, j in new.items():
        new[i] = j * 2
    return new
