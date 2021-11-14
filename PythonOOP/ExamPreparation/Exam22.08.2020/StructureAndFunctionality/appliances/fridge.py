from StructureAndFunctionality.appliances.appliance import Appliance


class Fridge(Appliance):
    DEFAULT_COST = 1.2

    def __init__(self):
        super().__init__(Fridge.DEFAULT_COST)
