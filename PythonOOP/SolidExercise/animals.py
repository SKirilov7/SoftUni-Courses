from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return 'meow'


class Dog(Animal):
    def make_sound(self):
        return 'woof-woof'


class Chicken(Animal):
    def make_sound(self):
        return 'kukuriguuuu'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat("Pesho"), Dog('Ivan'), Chicken('Miro')]
animal_sound(animals)


