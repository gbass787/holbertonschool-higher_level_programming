#!/usr/bin/python3
'''returns True if object is inherited'''

def inherits_from(obj, a_class):
    '''returns True if object is inherited'''

    if issubclass(type(obj), a_class):
        return True
    return False
