from StructureAndFunctionality.rooms.room import Room


class AloneOld(Room):
    DEFAULT_MEMBERS_COUNT = 1

    def __init__(self, family_name, pension):
        super().__init__(family_name, pension, AloneOld.DEFAULT_MEMBERS_COUNT)
        self.room_cost = 10

