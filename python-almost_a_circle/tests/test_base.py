#!/usr/bin/python3
'''Unittest for Base'''
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    '''tests class Base'''

    @classmethod
    def setUp(self):
        '''testing objects or instance'''

        Base._Base__nb_objects = 0
        self.b1 = Base()
        self.b2 = Base(42)
        self.b3 = Base(150)
        self.b4 = Base("hey")
        self.b5 = Base(-1.5)
        self.b6 = Base([1, 2, 3])
        self.b7 = Base()

    def test_empty(self):
        '''Validates for empty'''

        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b7.id, 2)

    def test_constructor_with_ids(self):
        '''Validates for non-empty'''

        self.assertEqual(self.b2.id, 42)
        self.assertEqual(self.b3.id, 150)
        self.assertEqual(self.b4.id, "hey")
        self.assertEqual(self.b5.id, -1.5)
        self.assertEqual(self.b6.id, [1, 2, 3])

    def test_to_json_string(self):
        '''testing to_json_string'''

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_string(self):
        '''testing from_json_string'''

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
