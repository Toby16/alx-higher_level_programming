#!/usr/bin/python3
"""
class Node
"""


class Node:
    """
    defines a node of a singly linked list
    Attributes:
        data
        next_node
    """
    def __init__(self, data, next_node=None):
        """
        init method for class 'Node'
        Args:
            data
            next_node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        method for class 'Node'
        private instance attribute: data
        property
        Returns:
            data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        method for class 'Node'
        property setter
        Arguments:
            value
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        private instance attribute: next_node
        property
        Returns:
            next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        property setter
        Arguments:
            value
        """
        if not isinstance(value, Node) and (value is not None):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

# ______________________________________________________________________________


"""
class SinglyLinkedList
"""


class SinglyLinkedList:
    """
    represents a singly linked list
    """
    def __init__(self):
        """
        init method for class 'SinglyLinkedList'
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        insert newnode to SinglyLinkedList in ascending order
        """
        newnode = Node(value)

        if self.__head is None:
            newnode.next_node = None
            self.__head = newnode
        elif self.__head.data > value:
            newnode.next_node = self.__head
            self.__head = newnode
        else:
            temp = self.__head
            while ((temp is not None) and (temp.next_node is not None) and
                    (temp.next_node.data < value)):
                temp = temp.next_node
            newnode.next_node = temp.next_node
            temp.next_node = newnode

    def __str__(self):
        """
        SinglyLinkedList representation
        """
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
