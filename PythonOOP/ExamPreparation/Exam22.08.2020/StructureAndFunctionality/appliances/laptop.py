from StructureAndFunctionality.appliances.appliance import Appliance


class Laptop(Appliance):
    DEFAULT_COST = 1

    def __init__(self):
        super().__init__(Laptop.DEFAULT_COST)

