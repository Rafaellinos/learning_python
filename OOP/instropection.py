"""
    function dir() shows all objects that the instance has access to
"""

class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("Logged in")

class PlayerWizard(User):
    def __init__(self, name, power, email):
        super().__init__(email) # same as User.__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"{self.name} attacks with power of {self.power}")


wizard1 = PlayerWizard("Merlin", 100, "merlin@email.com")
print(dir(wizard1))
"""
dir output:
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
'__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attack', 'email', 'name', 'power', 'sign_in']
"""
