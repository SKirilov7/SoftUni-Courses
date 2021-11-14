from StructureAndFunctionality.appliances.appliance import Appliance


class TV(Appliance):
    DEFAULT_COST = 1.5

    def __init__(self):
        super().__init__(TV.DEFAULT_COST)
