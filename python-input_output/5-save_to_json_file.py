#!/usr/bin/python3
'''writes an object to a text file'''


def save_to_json_file(my_obt, filename):
    '''writes an object to a text file'''
    import json
    with open(filename, 'w') as f:
        json.dump(my_obt, f)
