class Animal:
    """
        the class Animal is an example of encapsulation.
        when I access methods of the class, i'm accessing the encpsulated methods
    """
    def __init__(self, kingdom, class_type):
        self.kingdom = kingdom
        self.class_type = class_type

    def inform(self):
        return f"animal kingdom is {self.kingdom} and the class is {self.class_type}"


dog = Animal("Animalia","Mamalia")
print(dog.inform()) 
# dog.inform() is an abstraction, bacause its doesn't matter how the inform is implemented
# you can just use it without concern how its working, is abstracted for us