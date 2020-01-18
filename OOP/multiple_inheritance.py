"""
    Multiple inheritance
"""
class User():
    def sign_in(self):
        print("Logged in")

class Wizard(User):
    def __init__(self, name, power):
        self._name = name
        self._power = power
    def attack(self):
        return (f"Attacking with {self._power}")

class Archer(User):
    def __init__(self, name, arrows):
        self._name = name
        self._arrows = arrows
    def check_arrows(self):
        return (f"{self._arrows} arrows left")

    def run(self):
        return ("Ran really fast")

class HybridBord(Wizard, Archer):
    """
        if you u init without passing which class you are initializing, the first one
        inherited will be used.
    """
    def __init__(self, name, power, arrows):
        #need to use two inits in order to use power() from wizard and check_arrows from archer.
        Archer.__init__(self, name, arrows) 
        Wizard.__init__(self, name, power)
        

hb1 = HybridBord("Borguie", 50, 100)
print(hb1.check_arrows())
print(hb1.attack())
