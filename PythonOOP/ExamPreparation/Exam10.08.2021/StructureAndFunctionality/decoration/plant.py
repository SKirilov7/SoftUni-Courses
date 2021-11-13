from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    DEFAULT_PLANT_COMFORT = 5
    DEFAULT_PLANT_PRICE = 10

    def __init__(self):
        super().__init__(Plant.DEFAULT_PLANT_COMFORT, Plant.DEFAULT_PLANT_PRICE)
