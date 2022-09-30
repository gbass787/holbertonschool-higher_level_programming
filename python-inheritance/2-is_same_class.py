#!/usr/bin/python3
'''returns true if object is the same class'''


def is_same_class(obj, a_class):
    '''returns true if object is the same class'''

    if type(obj) is not a_class:
        return False
    return True
