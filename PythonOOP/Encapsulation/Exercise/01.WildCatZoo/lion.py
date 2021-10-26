from project.animal import Animal


class Lion(Animal):
    MONEY_TO_CARED_FOR = 50

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, Lion.MONEY_TO_CARED_FOR)
