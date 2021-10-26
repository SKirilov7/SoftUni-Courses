from project.animal import Animal


class Tiger(Animal):
    MONEY_TO_CARED_FOR = 45

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, Tiger.MONEY_TO_CARED_FOR)