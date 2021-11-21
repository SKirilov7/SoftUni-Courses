from StructureAndFunctionality.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    DEFAULT_OXYGEN = 50

    def __init__(self, name):
        super().__init__(name, Geodesist.DEFAULT_OXYGEN)





