#!/usr/bin/python3
'''class of a student'''


class Student:
    '''class of a student'''
    def __init__(self, first_name, last_name, age):
        '''initializer for student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''retrieves a dictionary representation'''
        return self.__dict__
