from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    DEFAULT_ORNAMENT_COMFORT = 1
    DEFAULT_ORNAMENT_PRICE = 5

    def __init__(self):
        super().__init__(Ornament.DEFAULT_ORNAMENT_COMFORT, Ornament.DEFAULT_ORNAMENT_PRICE)
