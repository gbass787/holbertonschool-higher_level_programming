#!/usr/bin/python3
'''writes a string to text file'''


def write_file(filename="", text=""):
    '''writes a string to text file'''

    with open(filename, 'w') as f:
        return f.write(text)
