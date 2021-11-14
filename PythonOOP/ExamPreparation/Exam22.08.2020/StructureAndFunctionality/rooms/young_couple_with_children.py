from StructureAndFunctionality.appliances.fridge import Fridge
from StructureAndFunctionality.appliances.laptop import Laptop
from StructureAndFunctionality.appliances.tv import TV
from StructureAndFunctionality.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        default_members_count = 2 + len(children)
        super().__init__(family_name, salary_one + salary_two, default_members_count)
        self.children.extend([child for child in children])
        self.room_cost = 30

        self.appliances = [TV(), Fridge(), Laptop()] * default_members_count
        self.calculate_expenses(self.appliances, self.children)
