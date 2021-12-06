from abc import ABC, abstractmethod


class Table(ABC):
    @abstractmethod
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, number_of_people):
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food):
        self.food_orders.append(baked_food)

    def order_drink(self, drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        return sum([food.price for food in self.food_orders]) + sum([drink.price for drink in self.drink_orders])

    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            result = f"Table: {self.table_number}\nType: {self.__class__.__name__}\nCapacity: {self.capacity}"
            return result.strip()

    def table_products_orders(self, menu):
        result = f"Table {self.table_number} ordered:\n"
        if menu == 'Food':
            for product in self.food_orders:
                result += repr(product) + '\n'
        elif menu == 'Drinks':
            for product in self.drink_orders:
                result += repr(product) + '\n'
        return result.strip()


