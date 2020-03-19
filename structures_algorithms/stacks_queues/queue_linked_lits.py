"""
queue are FIFO
First in, first out!
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = int()

    def peek(self):
        return self.bottom

    def enqueue(self, value):
        # add item in the top of the stack
        new_node = Node(value)
        if self.length == 0:
            self.bottom = new_node
        new_node.next = self.top
        self.top = new_node
        self.length += 1
        return self

    def dequeue(self):
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
