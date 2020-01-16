"""
    In python, there's no true private variables.
    That's why we use _ in front of variables or methods
    its a convention that is a private.
"""

class People:
    def __init__(self, name, age):
        self._name = name 
        # underscore is a convention for private variable.
        # It shows that the variable should not be modified
        self._age = age

    def say_name(self):
        return f"My name is {self.name}"
    
    def say_age(self):
        return f"My age is {self.age}"

rafael = People("Rafael", 28)
print(rafael.say_name())