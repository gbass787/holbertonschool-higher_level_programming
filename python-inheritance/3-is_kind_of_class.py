#!/usr/bin/python3
'''returns True if object is instance of class'''


def is_kind_of_class(obj, a_class):
    '''returns True if object is instance of class'''

    if isinstance(obj, a_class):
        return True
    return False
