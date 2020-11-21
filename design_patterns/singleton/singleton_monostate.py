"""
    Instância que compartilhem o mesmo estado.
"""

class Borg:
    __shared_state = {"1":"2"}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass

b = Borg()
b1 = Borg()

b.x = 4

print("Borg Object 'b':", b)  # b e b1 são objetos distintos
print("Borg Object 'b1':", b1)
print("Object State 'b':", b.__dict__)
print("Object state 'b1':", b1.__dict__)  # b e b1 compartilham o mesmo estado