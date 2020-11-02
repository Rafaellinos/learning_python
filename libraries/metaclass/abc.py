from abc import ABCMeta, abstractmethod



class Base(metaclass=ABCMeta):

    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


#b = Base()
"""
TypeError: Can't instantiate abstract class Base with abstract methods bar, foo
"""

class Concrete(Base):

    def foo(self):
        pass

    def bar(self):
        pass


c = Concrete()
"""
Caso nao defina bar:
TypeError: Can't instantiate abstract class Concrete with abstract methods bar
"""

"""
Precisa criar todos os abstract methods para não dar type erro
"""