

class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called")
        else:
            print("Instance already created", self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s = Singleton() # A classe é inicializada, mas o objeto nao é criado
print(s)
Singleton.get_instance() # o objeto é criado aqui
s1 = Singleton() # já criado