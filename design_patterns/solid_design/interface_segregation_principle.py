# ISP

class Machine:

    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class Multifunctional(Machine):

    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass

class OldFashionedPrinter(Machine):

    def print(self, document):
        pass # ok

    def fax(self, document):
        pass # noop

    def scan(self, document):
        """Not supported"""
        pass
    
# ao invés de ter a classe Machine,
# usar a classe Printer, Scanner e Fax
# Tendo uma interface para função

class Printer:
    @abstractmethod
    def print(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan(self, document)
        pass

class MyPrinter(Printer):
    def print(self, document):
        print(document)

class Photocopier(Pinter, Scanner):
    def print(self, document):
        pass

    def fax(self, document):
        pass