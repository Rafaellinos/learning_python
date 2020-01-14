#OOP

class PlayerCharcter:
    """
        self represents the instance of the class.
        With this keyword, its possible to access atributes and methods of the class.
        When objects are instantiated, the object itself is passed into the self parameter.

    """
    membership = True # class object attribute
    # class attribute is not dynamic
    def __init__(self, name="anonymous",age=0):
        # init method is a special method or a dunder method
        # automatically call when instantiate an object
        if self.membership: # or could be PlayerCharcter.membership because its a class obj attribute
            self.name = name # attributes
            self.age = age
        else:
            print("Not a membership")
        
    def run(self):
        return f"{self.name} run"
        # can't do PlayerCharcter.name because its not a class attribute, its refers to a instanceated object


player1 = PlayerCharcter("Cindy")
player2 = PlayerCharcter("Tom")
# instantiate, needs to give the init arguments
print(player1.name)
print(player2.name)
print(player1.run())
# help(player1) show the code
player1.membership = False
print(player1.membership)