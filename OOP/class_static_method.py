class Dog:

    animal_type = "mammal"

    def __init__(self, name="",age=0):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says AUAU"

    @classmethod
    # must use cls instead of self in classmethod
    def adding_thing(cls, num1, num2):
        
        #its possible to instantiate the class itself by using cls
        dog_inside = cls("Mark",1)
        print(dog_inside.bark())
        ##
        print(cls.animal_type) # can access the class attributes aswell
        ##
        return num1+num2
    
    @staticmethod
    def power_number(num1, num2):
        """
            with staticmethod its possible to use to call a method without instantiating.
            But its not possible to use cls or instantiate the class itself.
        """
        return num1 ** num2
    

rex_dog = Dog("Rex",3)

print(rex_dog.bark())
print(Dog.adding_thing(2,3)) # by using classmethod, its possible to call a method without instantiating
print(Dog.power_number(2,3)) # much like the classmethod, with static method its possible to call a method without instantiating
