from StructureAndFunctionality.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    DEFAULT_SIZE = 3

    def __init__(self, name, species, price):
        super().__init__(name, species, FreshwaterFish.DEFAULT_SIZE, price)

    def eat(self):
        self.size += 3
