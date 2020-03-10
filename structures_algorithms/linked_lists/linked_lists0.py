"""
First is head, last is tail.
Sets of nodes, two elements, the value and pointer for the next pointer.
Ex:
        head                              tail
 |(5, pointer)|->|(10, pointer)| -> |(2, pointer)| -> null

 Keep pointing to the next element until reach the null ending.
 Null terminator.

 The pointer is just a reference for a place in memory.
 Like two objects pointing to the same location in memory.
"""

basket = ['apples', 'grapes', 'pears']
# linked list: apples --> grapes --> pears --> null

"""
apples
 8957 ---> grapes
            8742 ---> pears
                       372  ---> null
                       
It points to the next element in memory.
https://visualgo.net/en/list

The main difference between arrays and linked list is that lists
have index's and if we want to get an item in the list, we just use
the index, but with linked lists, we need to traverse (loop through).
 
The item in the linked lists are also stored anywhere in the memory,
while in the normal lists they are stored next to each other.

Operation:

prepend: O(1) -> add item in first position
append: O(1) -> add item in last position
lookup: O(n) -> search for item
insert: O(n) -> add item anywhere between head and tail
delete: O(n) -> delete an item
"""

# Example: 10 --> 5 --> 16

class LinkedList(object):

    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None
        }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        """
            We create a new obj, update the next in the tail to point
            to that obj, updates the head aswell, because they are
            pointing to the same obj. For last, update the tail to be
            the new node.
        """
        # create a new node obj
        new_node = {
            'value': value,
            'next': None
        }
        # update the current tail to point to the next obj
        self.tail.update({
            'next': new_node})
        # update the tail to be the item that we created
        self.tail = new_node
        # obj: next and the tail are the same obj
        self.length += 1

        return self

    def prepand(self, value):
        new_node = {
            'value': value,
            'next': self.head
        }
        self.head = new_node
        self.length += 1
        return self

    def __str__(self):
        return str(self.__dict__)

my_ll = LinkedList(10)
print(my_ll)
my_ll.append(5)
my_ll.append(16)
print(my_ll)
# value: 10, next: {value 5, next: {value 16, next: None}}}
# 10 -> 5 -> 16
# 1 -> 10 -> 5 -> 16
my_ll.prepand(1)
print(my_ll)
# value: 1, next: {value: 10, next: {value 5, next: {value 16, next: None}}}}
