from project.animal import Animal


class Cheetah(Animal):
    MONEY_TO_CARED_FOR = 60

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, Cheetah.MONEY_TO_CARED_FOR)