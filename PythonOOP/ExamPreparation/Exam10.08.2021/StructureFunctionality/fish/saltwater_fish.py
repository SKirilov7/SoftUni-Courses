from StructureAndFunctionality.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    DEFAULT_SIZE = 5

    def __init__(self, name, species, price):
        super().__init__(name, species, SaltwaterFish.DEFAULT_SIZE, price)

    def eat(self):
        self.size += 2

