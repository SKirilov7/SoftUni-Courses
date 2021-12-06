from StructureAndFunctionality.aquarium.freshwater_aquarium import FreshwaterAquarium
from StructureAndFunctionality.aquarium.saltwater_aquarium import SaltwaterAquarium
from StructureAndFunctionality.decoration.decoration_repository import DecorationRepository
from StructureAndFunctionality.decoration.ornament import Ornament
from StructureAndFunctionality.decoration.plant import Plant
from StructureAndFunctionality.fish.freshwater_fish import FreshwaterFish
from StructureAndFunctionality.fish.saltwater_fish import SaltwaterFish


class Controller:
    VALID_AQUARIUM_TYPES = {
        'FreshwaterAquarium': FreshwaterAquarium,
        'SaltwaterAquarium': SaltwaterAquarium
    }
    VALID_DECORATION_TYPES = {
        'Ornament': Ornament,
        'Plant': Plant
    }
    VALID_FISH_TYPES = {
        'FreshwaterFish': FreshwaterFish,
        'SaltwaterFish': SaltwaterFish
    }

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type, aquarium_name):
        if aquarium_type not in Controller.VALID_AQUARIUM_TYPES:
            return "Invalid aquarium type."
        new_aquarium = Controller.VALID_AQUARIUM_TYPES[aquarium_type](aquarium_name)
        self.aquariums.append(new_aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        if decoration_type not in Controller.VALID_DECORATION_TYPES:
            return "Invalid decoration type."
        new_decoration = Controller.VALID_DECORATION_TYPES[decoration_type]()
        self.decorations_repository.add(new_decoration)
        return f"Successfully added {decoration_type}."

    @staticmethod
    def find_searched_aquarium(aquarium_name, aquariums):
        for aquarium in aquariums:
            if aquarium.name == aquarium_name:
                return aquarium

    def insert_decoration(self, aquarium_name, decoration_type):
        searched_aquarium = Controller.find_searched_aquarium(aquarium_name, self.aquariums)
        if not searched_aquarium:
            return None
        searched_decoration = self.decorations_repository.find_by_type(decoration_type)
        if not searched_decoration:
            return f"There isn't a decoration of type {decoration_type}."
        self.decorations_repository.remove(searched_decoration)
        searched_aquarium.add_decoration(searched_decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        searched_aquarium = Controller.find_searched_aquarium(aquarium_name, self.aquariums)
        if fish_type not in Controller.VALID_FISH_TYPES:
            return f"There isn't a fish of type {fish_type}."
        if searched_aquarium:
            new_fish = Controller.VALID_FISH_TYPES[fish_type](fish_name, fish_species, price)
            return searched_aquarium.add_fish(new_fish)

    def feed_fish(self, aquarium_name):
        searched_aquarium = Controller.find_searched_aquarium(aquarium_name, self.aquariums)
        if searched_aquarium:
            searched_aquarium.feed()
            return f"Fish fed: {len(searched_aquarium.fish)}"

    def calculate_value(self, aquarium_name):
        searched_aquarium = Controller.find_searched_aquarium(aquarium_name, self.aquariums)
        if searched_aquarium:
            return f"The value of Aquarium {aquarium_name} is {searched_aquarium.total_value:.2f}."

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += str(aquarium)
        return result.strip()
