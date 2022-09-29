#!/usr/bin/python3
'''A class that can not be modified'''


class LockedClass:
    '''class can nit have attributes modified'''
    __slots__ = ["first_name"]

    def __init__(self, value=""):
        self.first_name = value
