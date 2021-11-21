from StructureAndFunctionality.astronaut.astronaut_repository import AstronautRepository
from StructureAndFunctionality.astronaut.biologist import Biologist
from StructureAndFunctionality.astronaut.geodesist import Geodesist
from StructureAndFunctionality.astronaut.meteorologist import Meteorologist
from StructureAndFunctionality.planet.planet import Planet
from StructureAndFunctionality.planet.planet_repository import PlanetRepository


class SpaceStation:
    VALID_ASTRONAUT_TYPE_MAPPER = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist
    }

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.unsuccessful_missions = 0

    def add_astronaut(self, astronaut_type, name):
        # maybe it wont work like this.
        if astronaut_type not in SpaceStation.VALID_ASTRONAUT_TYPE_MAPPER:
            raise Exception("Astronaut type is not valid!")
        new_astronaut = SpaceStation.VALID_ASTRONAUT_TYPE_MAPPER[astronaut_type](name)
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."
        self.astronaut_repository.add(new_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name, items):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        new_planet = Planet(name)
        items_list = items.split(', ')
        new_planet.items.extend(items_list)
        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        astronaut_to_retire = self.astronaut_repository.find_by_name(name)
        if not astronaut_to_retire:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut_to_retire)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    @staticmethod
    def suitable_astronauts_for_mission(astronauts):
        suitable_astronauts = [astronaut for astronaut in astronauts if astronaut.oxygen > 30]
        suitable_astronauts.sort(key=lambda x: x.oxygen, reverse=True)
        if len(suitable_astronauts) > 5:
            return suitable_astronauts[:5]
        return suitable_astronauts

    def send_on_mission(self, planet_name):
        planet_to_send = self.planet_repository.find_by_name(planet_name)
        if not planet_to_send:
            raise Exception("Invalid planet name!")
        astronauts_for_mission = SpaceStation.suitable_astronauts_for_mission(self.astronaut_repository.astronauts)
        if not astronauts_for_mission:
            raise Exception("You need at least one astronaut to explore the planet!")
        astronauts_participated = 0
        for astronaut in astronauts_for_mission:
            astronauts_participated += 1
            while astronaut.oxygen > 0 and len(planet_to_send.items) > 0:
                astronaut.backpack.append(planet_to_send.items.pop())
                astronaut.breathe()
            if len(planet_to_send.items) == 0:
                self.successful_missions += 1
                return f"Planet: {planet_name} was explored. {astronauts_participated}" \
                       f" astronauts participated in collecting items."
        self.unsuccessful_missions += 1
        return "Mission is not completed."

    def report(self):
        result = f"{self.successful_missions} successful missions!\n" \
                 f"{self.unsuccessful_missions} missions were not completed!\n" \
                 f"Astronauts' info:\n"
        for astronaut in self.astronaut_repository.astronauts:
            result += repr(astronaut)
        return result








