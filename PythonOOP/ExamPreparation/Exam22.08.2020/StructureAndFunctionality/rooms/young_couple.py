from StructureAndFunctionality.appliances.fridge import Fridge
from StructureAndFunctionality.appliances.laptop import Laptop
from StructureAndFunctionality.appliances.tv import TV
from StructureAndFunctionality.rooms.room import Room


class YoungCouple(Room):
    DEFAULT_MEMBERS_COUNT = 2

    def __init__(self, family_name, salary_one, salary_two):
        super().__init__(family_name, salary_one + salary_two, YoungCouple.DEFAULT_MEMBERS_COUNT)
        self.room_cost = 20
        self.appliances = [TV(), Fridge(), Laptop()] * YoungCouple.DEFAULT_MEMBERS_COUNT
        self.calculate_expenses(self.appliances)

