class Everland:
    def __init__(self):
        self.rooms = []

    def check_room_paying_capability(self, expenses, room):
        if room.budget >= expenses:
            room.budget -= expenses
            return f"{room.family_name} paid {expenses:.2f}$ and have {room.budget:.2f}$ left."
        self.rooms.remove(room)
        return f"{room.family_name} does not have enough budget and must leave the hotel."

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_monthly_consumption = sum([room.expenses + room.room_cost for room in self.rooms])
        return f"Monthly consumption: {total_monthly_consumption:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            total_expenses = room.expenses + room.room_cost
            result.append(self.check_room_paying_capability(total_expenses, room))
        return '\n'.join(result)

    def status(self):
        result = f"Total population: {sum([room.members_count for room in self.rooms])}\n"
        for room in self.rooms:
            result += room.__repr__()

        return result
