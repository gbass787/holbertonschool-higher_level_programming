#!/usr/bin/python3
'''Base class'''
import json


class Base:
    '''To manage all your future classes and to avoid'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initialize class'''

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(dictionaries):
        '''return the JSON string'''

        if dictionaries is None or len(dictionaries) == 0:
            return "[]"
        return json.dumps(dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string'''

        with open(cls.__name__ + ".json", 'w') as f:
            dicts = []
            if list_objs is not None:
                dicts = [i.to_dictionary() for i in list_objs]
            f.write(cls.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string'''

        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with attributes'''

        dummy = cls(**dictionary)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''Opens a file and returns a list'''

        j_list = None
        try:
            with open(cls.__name__ + ".json") as f:
                j_list = cls.from_json_string(f.read())
        except:
            return []
        return [cls.create(**x) for x in j_list]
