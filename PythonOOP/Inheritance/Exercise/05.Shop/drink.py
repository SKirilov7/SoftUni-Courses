from project.product import Product


class Drink(Product):
    DRINK_QUANTITY = 10

    def __init__(self,name):
        super().__init__(name, Drink.DRINK_QUANTITY)

