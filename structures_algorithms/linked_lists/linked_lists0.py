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

class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):

    def __init__(self, value):
        node = Node(value)
        # instead of doing dict, its better to create
        # an node obj
        # self.head = {
        #     'value': value,
        #     'next': None
        # }
        self.head = node
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        # create new node obj
        self.tail.next = new_node
        # add the tail the new node
        self.tail = new_node
        # update the tail to be the last item
        self.length += 1
        return self

    def prepand(self, value):
        new_node = Node(value)
        # create new node obj
        new_node.next = self.head
        # add next obj as the head (first node)
        self.head = new_node
        # make the new_node as the head
        self.length += 1
        return self

    def insert(self, index, value):
        if index > self.length or index < 0:
            raise Exception("Invalid index")
        elif index == 0:
            self.prepand(value)
            return self
        elif index == self.length:
            self.append(value)
            return self

        new_node = Node(value)
        obj = self.head
        obj_current = obj
        i = 0
        while i <= self.length:
            if i == index:
                obj_current.next = new_node
                new_node.next = obj
                break
            obj_current = obj
            obj = obj.next
            i += 1

        self.length += 1
        return self

    def __str__(self):
        obj = self.head
        string = str()
        for _ in range(my_ll.length):
            string += str(obj.value)+"->"
            obj = obj.next
        string += "Null"
        return string


my_ll = LinkedList(10)
# 10 -> null
my_ll.append(5)
# 10 -> 5 -> null
my_ll.append(16)
# 10 -> 5 -> 16 -> null
my_ll.prepand(1)
# 1 -> 10 -> 5 -> 16 -> null
print(my_ll)
# 1 -> 10 -> 99 -> 5 -> 16 -> null
print(my_ll.length)
my_ll.insert(2, 99)
print(my_ll.length)
print(my_ll)


