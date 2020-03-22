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
        return self.top

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
            self.length += 1
            return self
        self.bottom.next = new_node
        self.bottom = new_node
        self.length += 1
        return self

    def dequeue(self):
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


my_queue = Queue()
my_queue.enqueue('Joy')
my_queue.enqueue('Matt')
my_queue.enqueue('Pavel')
my_queue.enqueue('Samir')
print(my_queue)
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())

