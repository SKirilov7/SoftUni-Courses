from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    VALID_FISH_TYPES_MAPPER = {
        'FreshwaterFish': FreshwaterFish,
        'SaltwaterFish': SaltwaterFish
    }
    VALID_FISH_AQUARIUMS = {
        'FreshwaterAquarium': FreshwaterAquarium,
        'SaltwaterAquarium': SaltwaterAquarium
    }
    VALID_DECORATION_MAPPER = {
        'Plant': Plant,
        'Ornament': Ornament
    }

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    @staticmethod
    def find_searched_aquarium(aquarium_name, aquariums):
        for aquarium in aquariums:
            if aquarium.name == aquarium_name:
                return aquarium

    def add_aquarium(self, aquarium_type, aquarium_name):
        if aquarium_type not in self.VALID_FISH_AQUARIUMS:
            return "Invalid aquarium type."
        new_aquarium = self.VALID_FISH_AQUARIUMS[aquarium_type](aquarium_name)
        self.aquariums.append(new_aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        if decoration_type not in self.VALID_DECORATION_MAPPER:
            return "Invalid decoration type."
        new_decoration = self.VALID_DECORATION_MAPPER[decoration_type]()
        self.decorations_repository.add(new_decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name, decoration_type):
        searched_aquarium = self.find_searched_aquarium(aquarium_name, self.aquariums)
        wanted_decoration = self.decorations_repository.find_by_type(decoration_type)
        if not searched_aquarium:
            return
        if not wanted_decoration == 'None':
            searched_aquarium.add_decoration(wanted_decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."
        return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in self.VALID_FISH_TYPES_MAPPER:
            return f"There isn't a fish of type {fish_type}."
        searched_aquarium = self.find_searched_aquarium(aquarium_name, self.aquariums)
        fish_to_add = self.VALID_FISH_TYPES_MAPPER[fish_type](fish_name, fish_species, price)
        if searched_aquarium:
            return searched_aquarium.add_fish(fish_to_add)

    def feed_fish(self, aquarium_name):
        searched_aquarium = self.find_searched_aquarium(aquarium_name, self.aquariums)
        if searched_aquarium:
            searched_aquarium.feed()
            return f"Fish fed: {len(searched_aquarium.fish)}"

    def calculate_value(self, aquarium_name):
        searched_aquarium = self.find_searched_aquarium(aquarium_name, self.aquariums)
        if searched_aquarium:
            result = searched_aquarium.calculate_price()
            return f"The value of Aquarium {aquarium_name} is {result:.2f}."

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += aquarium.__str__()
        return result






