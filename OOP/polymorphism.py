"""
    Polymorphism:
    Poly means many and morphism means forms, many form in other words.
    In python means that objects can share the same names but work in diferent ways.

"""

class User:
    def attack(self):
        return "do nothing"

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(User.attack(self))
        return f"{self.name} uses {self.arrows} arrows"
####

archer1 = Archer("Robin", 30)
print(archer1.attack())

def player_attack(player):
    print(player.attack())

player_attack(archer1) # in polymorphism, we can use objects by passing through classes and methods
