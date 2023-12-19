#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        """Define a node of a Singly Linked list"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Data Getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """Data Setter"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Next_node Getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Next_node Setter"""
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        """Define a Singly Linked list"""
        self.__head = None

    def sorted_insert(self, value):
        ne = Node(value)
        he = self.__head
        start = False

        if not self.__head:
            self.__head = ne
            new.next_node = None
        else:
            if value < self.__head.data:
                start = True
            while he.next_node and value > he.next_node.data\
                    and not add_start:
                he = he.next_node
            if not start:
                    ne.next_node = he.next_node
                    he.next_node = ne
            else:
                ne.next_node = he
                self.__head = ne
            new.data = value

    def __str__(self):
        a = ""
        cur = self.__head

        while current:
            a += str(cur.data) + '\n'
            cur = cur.next_node
        return a[: -1]
