class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.top = None
        self.bottom = None
        self.index = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        new_node = Node(x)
        if self.index == 0:
            self.top = new_node
            self.bottom = new_node
            self.index += 1
            return None
        self.bottom.next = new_node
        self.bottom = new_node
        self.index += 1
        return None

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        top_node = self.top
        self.top = self.top.next
        self.index -= 1
        return top_node.value

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.top.value

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.index <= 0:
            return True
        return False


my_queue = MyQueue()
my_queue.push(1)
print(my_queue.peek())
my_queue.push(2)
print(my_queue.peek())
print(my_queue.pop())
print(my_queue.peek())
print(my_queue.empty())

print(my_queue.pop())
print(my_queue.empty())