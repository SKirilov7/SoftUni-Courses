from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass

    @staticmethod
    def which_animal_which_food_eats():
        return {
            'Owl': ['Meat'],
            'Hen': ['Vegetable', 'Fruit', 'Seed', 'Meat'],
            'Mouse': ['Vegetable', 'Fruit'],
            'Dog': ['Meat'],
            'Cat': ['Vegetable', 'Meat'],
            'Tiger': ['Meat']
        }

    def is_appropriate_food(self, food):
        food_eaten_by_who = self.which_animal_which_food_eats()
        return food.__class__.__name__ in food_eaten_by_who[self.__class__.__name__]

    def return_error_wrong_food(self, food):
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

    def gain_weight(self, food, amount_per_quantity):
        self.food_eaten += food.quantity
        self.weight += amount_per_quantity * food.quantity


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
