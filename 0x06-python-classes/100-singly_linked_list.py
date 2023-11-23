#!/usr/bin/python3
"""Module of Node and Linked List classes

The module contains class definitions of a Node and Linkedlist

Classes:
    Node: A Linked List's node structure
    SinglyLinkedList: a singly linked list's class
"""


class Node():
    """Definition of a singly linked list's node

    Attributes:
        __init__: the node's initialisation method.
        data: the value at the corresponding node
            * default so None
            * if is not None and not of type int, a TypeError
                is raised.
        next_node: the list's next_node.
            * defaulst to None
            * if not None and is not of type Node, a TypeError
                is raised
        @property:
            data: returns the node's data
                * has its setter method
                * if value given is not of type int, a TypeError
                    is raised as with __init__
            next_node: returns the list's next node
                * has its setter defined
                * if value given is not of type Node, a TypeError
                    is raised as with __init__
    """
    def __init__(self, data=None, next_node=None):
        if data is None or not isinstance(data, int):
            raise TypeError("data must be an integer")
        if not isinstance(next_node, Node) and next_node:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """List data property getter

        Returns:
            node's data
        """
        return self.__data

    @property
    def next_node(self):
        """List's next node property getter

        Returns:
            the list's next node object
        """
        return self.__next_node

    @data.setter
    def data(self, value):
        if value is None or not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList():
    """Singly linked list class definition

    Attributes:
        __init__: class initialisation method.
        head(:obj: Node): the list's head. Defaults to None
            * cannot be modified outside of the sorted_insert method
        sorted_insert: a method that inserts into the linked list
            a new value with values in list sorted in ascending order.
            * if value is not of type int, a TypeError is raised
                as with Node
            * it modifies the list internally including the __head
                private attribute.
        @property
            head(:obj: Node): returns list's head object
            print: prints list's node values(data)
            len(:obj: int): returns the list's length
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Method to insert into list in sorted manner

        Method inserts into a linked list a new value at a
            position that ultimately sorts the list members
            in ascending order, from least to greatest.
            * if value is not of type int, a TypeError
                is raised as with Node __init__
            * it modifies the list's head node if necessary

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        new_node = Node(value)
        if not self.__head:
            self.__head = new_node
        else:
            temp = self.__head
            prev = self.__head
            while temp and temp.data <= value:
                prev = temp
                temp = temp.next_node
            if not temp:
                prev.next_node = new_node
            else:
                new_node.next_node = temp
                if temp is self.__head:
                    self.__head = new_node
                else:
                    prev.next_node = new_node

    @property
    def head(self):
        """Linked list's head getter

        Returns:
            (:obj: Node): the list's head Node
        """
        return self.__head

    @property
    def print(self):
        """Prints linked list to stdout

        Returns:
            None
        """
        node = self.__head
        while node:
            print(node.data)
            node = node.next_node

    @property
    def length(self):
        """Linked lists' length getter

        Returns:
            (:obj: int): the list's length (total number of nodes)
        """
        count = 0
        temp = self.__head
        while temp:
            count += 1
            temp = temp.next_node
        return count
