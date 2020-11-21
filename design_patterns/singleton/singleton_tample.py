

class Singleton(object):

    def __new__(cls, *args, **kwargs): # Devolve o mesmo objeto
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s0 = Singleton()
print('Objeto Criado', s0)

s1 = Singleton()

print('Objeto 2 criado', s1)
