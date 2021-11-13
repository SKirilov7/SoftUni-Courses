from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    VALID_FISH_TYPES_MAPPER = [
        'FreshwaterFish',
        'SaltwaterFish'
    ]

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
        if not value:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([decoration.comfort for decoration in self.decorations])

    def add_fish(self, fish):
        if len(self.fish) >= self.capacity:
            return "Not enough capacity."
        fish_given_type = fish.__class__.__name__
        if fish_given_type in self.VALID_FISH_TYPES_MAPPER and fish.AQUARIUM_PREF == self.__class__.__name__:
            self.fish.append(fish)
            return f"Successfully added {fish_given_type} to {self.name}."
        return "Water not suitable."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        # maybe I need to look after the class name if is it Plant or Ornament.
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def calculate_price(self):
        return sum([fish.price for fish in self.fish]) + sum([dec.price for dec in self.decorations])

    def __str__(self):
        result = f"{self.name}:\nFish: {' '.join([fish.name for fish in self.fish]) if self.fish else 'none'}\n"

        total_comfort = self.calculate_comfort()
        result += f'Decorations: {len(self.decorations)}\nComfort: {total_comfort}\n'
        return result
