#!/usr/bin/python3
"""Defines a class Node"""


class Node:
    """Has a value and a reference to the next node"""

    def __init__(self, data, next_node=None):
        """Initializer"""

        self.data = data
        self.next_node = next_node

    def __str__(self):
        return self.__data

    @property
    def data(self):
        """getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter"""
        if value is None or type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Defines a Singly linked list"""

    def __init__(self):
        """Initializer"""
        self.__head = None
        """Private attribute, no setters or getters"""

    def __str__(self):
        """String representation of a SinglyLinkedList"""
        string = ""
        temp = self.__head
        while temp is not None:
            string += str(temp.data)
            temp = temp.next_node
            if temp is not None:
                string += "\n"
        return string

    def sorted_insert(self, value):
        """ that inserts a new Node"""
        new = Node(value)
        if self.__head is None:
            self.__head = new
        elif self.__head.data > new.data:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data <= new.data:
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new
