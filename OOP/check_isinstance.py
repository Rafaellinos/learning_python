class User(object): # object is hidden, but is inherited by default
    def sign_in(self):
        print("Logged in")

class Wizard(User):
    def __init__(self, name):
        self._name = name
    
    def says_name(self):
        print(f"My name is {self.name}")

wizard1 = Wizard("Merlin")

print(isinstance(wizard1, Wizard)) # returns True
#is instance checks if the objected is instance of a certains objects

print(isinstance(wizard1, User)) # returns True
# it also returns true if the object is child of the class

print(isinstance(wizard1, object)) # returns True
# every class inherits object by default and share the same base
# dunder methods, live mro