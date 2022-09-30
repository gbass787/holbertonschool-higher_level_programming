#!/usr/bin/python3
'''write a class MyInt, MyInt has == and != operatos inverted'''

class MyInt(int):
    '''class inherits from int'''
    def __init__(self, value):
        '''comments'''
        self.__value = value
