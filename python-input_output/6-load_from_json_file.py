#!/usr/bin/python3
'''creates an object from json file'''


def load_from_json_file(filename):
    '''creates an object from json file'''
    import json
    with open(filename) as f:
        return json.load(f)
