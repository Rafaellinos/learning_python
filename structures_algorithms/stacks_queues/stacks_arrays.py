class Stack(list):
    def __init__(self):
        super().__init__()

    def peek(self):
        # return item in the top of the stack
        return self[0]

    def push(self, value):
        # add item in the top of the stack
        self.insert(0, value)
        return self

    def pop(self):
        del self[0]
        return self

    def is_empty(self):
        if self.__len__() <= 0:
            print("Stack is empty")
            return True
        return False


my_stack = Stack()
my_stack.push('google')
my_stack.push('udemy')
my_stack.push('discord')
print(my_stack)
print(my_stack.peek())
print(my_stack.pop())