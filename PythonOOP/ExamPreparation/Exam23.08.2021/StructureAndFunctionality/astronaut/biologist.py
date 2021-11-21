from StructureAndFunctionality.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    DEFAULT_OXYGEN = 70

    def __init__(self, name):
        super().__init__(name, Biologist.DEFAULT_OXYGEN)

    def breathe(self):
        self.oxygen -= 5
