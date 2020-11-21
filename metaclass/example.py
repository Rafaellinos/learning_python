"""
    Possível criar classes com type.

    Considerado má prática
"""


class Foo:
    def show(self):
        print("hi")


def add_attribute(self):
    self.z = 9


Teste = type('Test', (Foo,), {"x": 5, "add_attribute": add_attribute})  # mesmo que criar uma classe

t = Teste()
print(t.show())
print(t.x)
t.add_attribute()
print(t.z)
