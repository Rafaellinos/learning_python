"""
Stacks:
    LIFO:
        Last in first out

       lookup O(n)
       pop    O(1)
       push   O(1)
       peek   O(1) # first item

       Best option to use is arrays, because the
       item is next to each other in memory, instead
       of linked lists, that stores randomly in memory.

       ex:
       array = []
       array.push(5)
       array.push(2)
       [5,2] -> indexes 0,1
       last in, its 2 of index 1, just pop.
Queues:
    FIFO:
        First in first out

        lookup  O(n)
        enqueue O(1)
        dequeue O(1) # takes out the first person
        peek    O(1) # last item


    Best option is linked lists, because each time that
    you remove some item from the queue, you need to shift
    the arrays, that's an O(n) operation.

    ex:
       array = []
       array.push(5)
       array.push(2)
       array.push(1)
       [5,2,1] -> indexes 0,1,2
       first in 5 of index 0, need to shift the array.
"""


# Stacks With LINKED LISTS
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = int()

    def peek(self):
        # return item in the top of the stack
        return self.top

    def push(self, value):
        # add item in the top of the stack
        new_node = Node(value)
        if self.length == 0:
            self.bottom = new_node
        new_node.next = self.top
        self.top = new_node
        self.length += 1
        return self

    def pop(self):
        # remove the top of the stack
        if self.is_empty():
            return
        next_node = self.top.next
        self.top = next_node
        if self.length == 1:
            self.bottom = None
        self.length -= 1
        return self

    def is_empty(self):
        if self.length <= 0:
            print("Stack is empty")
            return True
        return False

    def __str__(self):
        node = self.top
        string = str()
        for i in range(self.length):
            string += f"{node.value} "
            node = node.next
        return string


my_stack = Stack()
my_stack.push('google')
my_stack.push('udemy')
my_stack.push('discord')
print(my_stack)
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.bottom)
print(my_stack.pop())
