class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    @staticmethod
    def can_rent_room(bool_is_taken, capacity,people):
        return not bool_is_taken and people <= capacity

    def take_room(self, people):
        if self.can_rent_room(self.is_taken, self.capacity, people):
            self.guests += people
            self.is_taken = True
        else:
            return f"Room number {self.number} cannot be taken"

    def free_room(self):
        if self.is_taken:
            self.is_taken = False
            self.guests = 0
        else:
            return f"Room number {self.number} is not taken"




