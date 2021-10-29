from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

    def is_fuel_enough(self, fuel_needed, fuel_quantity):
        return fuel_needed <= self.fuel_quantity


class Car(Vehicle):
    AIR_CONDITIONER_BONUS_FUEL = 0.9

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + Car.AIR_CONDITIONER_BONUS_FUEL)
        if self.is_fuel_enough(fuel_needed, self.fuel_quantity):
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CONDITIONER_BONUS_FUEL = 1.6

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + Truck.AIR_CONDITIONER_BONUS_FUEL)
        if self.is_fuel_enough(fuel_needed, self.fuel_quantity):
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)