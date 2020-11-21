"""
    Criação de uma metaclass para servir como classe Abstrata.
    Então, o forestFactory é reposável por chamar a classe
"""
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def do_say(self):
        pass

class Dog(Animal):

    def do_say(self):
        print("Au au")

class Cat(Animal):

    def do_say(self):
        print("miau miau")


class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()

## Código do cliente

if __name__ == '__main__':
    ff = ForestFactory()
    animal = input("Qual animal deveria fazer um som, Dog ou Cat?")
    ff.make_sound(animal)