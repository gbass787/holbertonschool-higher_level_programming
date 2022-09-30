#!/usr/bin/python3
'''returns an object'''


def from_json_string(my_str):
    '''returns an object'''
    import json
    return json.loads(my_str)
