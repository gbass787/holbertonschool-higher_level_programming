#!/usr/bin/python3
'''appends a string to a text'''


def append_write(filename="", text=""):
    '''appends a string to a text'''

    with open(filename, 'a') as f:
        return f.write(text)
