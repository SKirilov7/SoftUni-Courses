from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    AQUARIUM_PREF = 'SaltwaterAquarium'
    DEFAULT_SIZE = 5

    def __init__(self, name, species, price):
        super().__init__(name, species, SaltwaterFish.DEFAULT_SIZE, price)

    def eat(self):
        self.size += 2

