from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    VALID_FISH_TYPES = ['FreshwaterFish', 'SaltwaterFish']
    VALID_FISH = None

    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    @property
    def total_value(self):
        return sum([fish.price for fish in self.fish]) + sum([decoration.price for decoration in self.decorations])

    def calculate_comfort(self):
        return sum([decoration.comfort for decoration in self.decorations])

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."
        fish_type = fish.__class__.__name__
        if fish_type in BaseAquarium.VALID_FISH_TYPES and fish_type == self.VALID_FISH:
            self.fish.append(fish)
            return f"Successfully added {fish_type} to {self.name}."
        return "Water not suitable."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        [fish.eat() for fish in self.fish]

    def __str__(self):
        fish = ' '.join([fish.name for fish in self.fish]) if self.fish else 'none'
        return f'''{self.name}:
Fish: {fish}
Decorations: {len(self.decorations)}
Comfort: {self.calculate_comfort()}
'''
