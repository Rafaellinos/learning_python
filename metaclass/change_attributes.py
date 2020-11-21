
"""
    Modificar os atributos.
    Metaclass define o comportamento da classe
"""
class Meta(type):

    def __new__(self, class_name, bases, attrs):

        a = {}
        for name, val in attrs.items(): # percorre os atributos e os transforma em upper
            if name.startswith("__"):
                a[name] = val
            else:
                a[name.upper()] = val

        return type(class_name, bases, a)


class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        print("hi")


d = Dog()

print(d.X)
d.HELLO()