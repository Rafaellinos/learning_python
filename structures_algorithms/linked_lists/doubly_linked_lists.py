"""
The difference between the normal linked lists and doubly linked lists
are that the doubly also points to the previous node.

>> Doubly linked lists have a pointer to next and previous node in each obj.
"""


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList(object):
    # That a double linked list

    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node
        self.length += 1
        return self

    def prepend(self, value):
        new_node = Node(value)
        self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return self

    def _traverse(self, index):
        node = self.head
        if index <= 0:
            return node
        i = 0
        while i <= self.length:
            if i == index:
                return node
            node = node.next
            i += 1
        return node

    def _check_index(self, index):
        if index > self.length or index < 0:
            raise Exception("Invalid index")
        return True

    def insert(self, index, value):
        self._check_index(index)
        if index == 0:
            self.prepend(value)
            return self
        elif index == self.length:
            self.append(value)
            return self

        new_node = Node(value)

        previous_node = self._traverse(index - 1)

        current_node = previous_node.next
        previous_node.next = new_node
        new_node.previous = previous_node
        new_node.next = current_node
        current_node.previous = new_node
        self.length += 1
        return self

    def remove(self, index):
        self._check_index(index)

        if index <= 0:
            self.head = self.head.next
            self.head.previous = None
            self.length -= 1
            return self

        previous_node = self._traverse(index - 1)
        del_node = previous_node.next
        next_node = del_node.next
        previous_node.next = next_node
        next_node.previous = previous_node
        self.length -= 1

        return self

    def reverse_list(self):
        current_node = self.tail
        self.tail = self.head
        self.head = current_node

        i = 0
        while i < self.length:
            node = current_node.next
            current_node.next = current_node.previous
            current_node.previous = node
            current_node = current_node.next
            i += 1

        return self

    def __str__(self):
        obj = self.head
        string = str()
        for _ in range(self.length):
            string += str(obj.value) + "->"
            obj = obj.next
        string += "Null \n"

        obj_reverse = self.tail
        string += "Null"
        for _ in range(self.length):
            string += "<-"
            string += str(obj_reverse.value)
            obj_reverse = obj_reverse.previous

        return string


liked_list = LinkedList(1)
print(liked_list)  # 1 -> null
print(liked_list.append(20))  # 1 -> 20 -> null
print(liked_list.append(10))  # 1 -> 20 -> 10 -> null
print(liked_list.prepend(90))  # 90 -> 1 -> 20 -> 10 -> null
print(liked_list.insert(2, 3))  # 90 -> 1 -> 3 -> 20 -> 10 ->null
print(liked_list.remove(2))  # 90 -> 1 -> 20 -> 10 -> null
print(liked_list.reverse_list()) # 10 -> 20 -> 1 -> 90 -> null
