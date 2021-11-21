from StructureAndFunctionality.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    DEFAULT_OXYGEN = 90

    def __init__(self, name):
        super().__init__(name, Meteorologist.DEFAULT_OXYGEN)

    def breathe(self):
        self.oxygen -= 15


