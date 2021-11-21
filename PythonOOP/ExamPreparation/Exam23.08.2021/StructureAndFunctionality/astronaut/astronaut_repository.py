class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut):
        # maybe we should not check if is in it?
        if astronaut not in self.astronauts:
            self.astronauts.append(astronaut)

    def remove(self, astronaut):
        if astronaut in self.astronauts:
            self.astronauts.remove(astronaut)

    def find_by_name(self, name):
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut
