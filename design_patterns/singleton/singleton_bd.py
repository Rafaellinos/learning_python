"""
    Cenário real

    metaclass:

        Class Test:
            pass

        Test = type(Test) # return Type!!!

        Test = type('Test', (), {}) # Equivalente a criar uma class Teste: pass
"""
import sqlite3

class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kw):
        # usado para criar un Singleton. Ou seja, toda instancia de MetaSingleton será a mesma
        print(cls, args, kw, cls._instances)
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kw)
        print(cls, args, kw, cls._instances)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj

db1 = Database().connect()
db2 = Database().connect()

print("db1:", db1)
print("db1:", db2) # compartilham a mesma instância
