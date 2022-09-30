#!/usr/bin/python3
'''comments'''


def inherits_from(obj, a_class):
    ''''comments'''
    if isinstance(obj, a_class):
        if type(obj) is not a_class:
            return True
    return False
