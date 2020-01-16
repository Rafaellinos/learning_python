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
