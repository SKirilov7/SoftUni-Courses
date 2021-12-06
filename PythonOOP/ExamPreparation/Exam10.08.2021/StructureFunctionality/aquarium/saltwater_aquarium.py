from StructureAndFunctionality.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    VALID_FISH = 'SaltwaterFish'
    DEFAULT_CAPACITY = 25

    def __init__(self, name):
        super().__init__(name, SaltwaterAquarium.DEFAULT_CAPACITY)



