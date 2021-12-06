from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    VALID_FOOD_TYPES = {
        'Bread': Bread,
        'Cake': Cake
    }
    VALID_DRINK_TYPES = {
        'Tea': Tea,
        'Water': Water
    }
    VALID_TABLE_TYPES = {
        'InsideTable': InsideTable,
        'OutsideTable': OutsideTable
    }

    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type, name, price):
        if name in [food.name for food in self.food_menu] \
                and food_type in [food.__class__.__name__ for food in self.food_menu if food.name == name]:
            raise Exception(f"{food_type} {name} is already in the menu!")
        if food_type in Bakery.VALID_FOOD_TYPES:
            new_food = Bakery.VALID_FOOD_TYPES[food_type](name, price)
            self.food_menu.append(new_food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        if name in [drink.name for drink in self.drinks_menu] \
                and drink_type in [drink.__class__.__name__ for drink in self.drinks_menu if drink.name == name]:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        if drink_type in Bakery.VALID_DRINK_TYPES:
            new_drink = Bakery.VALID_DRINK_TYPES[drink_type](name, portion, brand)
            self.drinks_menu.append(new_drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        if table_type in Bakery.VALID_TABLE_TYPES:
            if table_number in [table.table_number for table in self.tables_repository]:
                raise Exception(f"Table {table_number} is already in the bakery!")
            new_table = Bakery.VALID_TABLE_TYPES[table_type](table_number, capacity)
            self.tables_repository.append(new_table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        for table in self.tables_repository:
            if table.capacity >= number_of_people and not table.is_reserved:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    @staticmethod
    def find_searched_table(table_num, tables):
        for table in tables:
            if table.table_number == table_num:
                return table

    def return_product_not_in_menu_and_order_available(self, products, table):
        products_not_in_menu = []
        food_menu = [p.name for p in self.food_menu]
        drink_menu = [p.name for p in self.drinks_menu]
        for product in products:
            if product in food_menu:
                table.order_food([f for f in self.food_menu if product == f.name][0])
            elif product in drink_menu:
                table.order_drink([d for d in self.drinks_menu if product == d.name][0])
            else:
                products_not_in_menu.append(product)
        result = f'\n{self.name} does not have in the menu:\n'
        for product_name in products_not_in_menu:
            result += f'{product_name}\n'
        return result

    def order_food(self, table_number, *foods):
        table_to_order = Bakery.find_searched_table(table_number, self.tables_repository)
        if not table_to_order:
            return f"Could not find table {table_number}"

        food_not_in_menu = self.return_product_not_in_menu_and_order_available(foods, table_to_order)
        result = table_to_order.table_products_orders('Food')
        result += food_not_in_menu
        return result.strip()

    def order_drink(self, table_number, *drinks):
        table_to_order = Bakery.find_searched_table(table_number, self.tables_repository)
        if not table_to_order:
            return f"Could not find table {table_number}"
        drinks_not_in_menu = self.return_product_not_in_menu_and_order_available(drinks, table_to_order)

        result = table_to_order.table_products_orders('Drinks')
        result += drinks_not_in_menu
        return result.strip()

    def leave_table(self, table_number):
        searched_table = Bakery.find_searched_table(table_number, self.tables_repository)
        if searched_table:
            bill = searched_table.get_bill()
            searched_table.clear()
            self.total_income += bill
            return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        result = ''
        for table in self.tables_repository:
            if not table.is_reserved:
                result += table.free_table_info()
                result += '\n'
        return result.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
