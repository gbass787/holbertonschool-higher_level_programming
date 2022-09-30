#!/usr/bin/python3
'''class of a student'''


class Student:
    '''class of a student'''
    def __init__(self, first_name, last_name, age):
        '''initializer for student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieves a dictionary representation'''
        clas = self.__dict__
        temp = dict()
        if attrs is not None:
            for i in attrs:
                if i in clas:
                    temp[i] = clas[i]
            return temp
        return clas
