"""
Example: Users can have any class like wizard, warrior, archer etc...
"""

class User():
    def sign_in(self):
        print("Logged in")

class Wizard(User):
    def __init__(self, name, power):
        self._name = name
        self._power = power
    def attack(self):
        print(f"Attacking with {self._power}")

class Archer(User):
    def __init__(self, name, arrows):
        self._name = name
        self._arrows = arrows
    def attack(self):
        print(f"Attacking with {self._arrows}")

wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 100)
wizard1.sign_in()
wizard1.attack()