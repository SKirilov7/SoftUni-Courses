from StructureAndFunctionality.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    VALID_FISH = 'FreshwaterFish'
    DEFAULT_CAPACITY = 50

    def __init__(self, name):
        super().__init__(name, FreshwaterAquarium.DEFAULT_CAPACITY)

