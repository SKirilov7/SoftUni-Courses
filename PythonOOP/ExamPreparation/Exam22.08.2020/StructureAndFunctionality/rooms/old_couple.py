from StructureAndFunctionality.appliances.fridge import Fridge
from StructureAndFunctionality.appliances.stove import Stove
from StructureAndFunctionality.appliances.tv import TV
from StructureAndFunctionality.rooms.room import Room


class OldCouple(Room):
    DEFAULT_MEMBERS_COUNT = 2

    def __init__(self, family_name, pension_one, pension_two):
        super().__init__(family_name, pension_one + pension_two, OldCouple.DEFAULT_MEMBERS_COUNT)
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove()] * OldCouple.DEFAULT_MEMBERS_COUNT
        self.calculate_expenses(self.appliances)

