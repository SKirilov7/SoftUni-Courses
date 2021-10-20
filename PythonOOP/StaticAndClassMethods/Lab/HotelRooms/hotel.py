class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room_searched = [r for r in self.rooms if r.number == room_number]
        if room_searched:
            room_searched = room_searched[0]
            if not room_searched.is_taken and room_searched.capacity >= people:
                self.guests += people
                room_searched.guests = people
                room_searched.is_taken = True

    def free_room(self, room_number):
        room_searched = [r for r in self.rooms if r.number == room_number]
        if room_searched:
            room_searched = room_searched[0]
            if room_searched.is_taken:
                current_amount_of_guests = room_searched.guests
                room_searched.is_taken = False
                room_searched.guests = 0
                self.guests -= current_amount_of_guests

    def status(self):
        result = f'Hotel {self.name} has {self.guests} total guests\n'
        result += f'Free rooms: {", ".join(str(r.number) for r in self.rooms if not r.is_taken)}\n'
        result += f'Taken rooms: {", ".join(str(r.number) for r in self.rooms if r.is_taken)}'
        return result





