#!/usr/bin/python3
"""Class of a list"""


class MyList(list):
    """A class from list'"""
    def print_sorted(self):
        """prints sorted list"""

        print(sorted(self))
