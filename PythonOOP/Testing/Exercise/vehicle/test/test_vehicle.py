from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(10.5, 100.5)

    def test_if_init_attaches_instance_attributes_correctly(self):
        self.assertEqual(10.5, self.vehicle.fuel)
        self.assertEqual(10.5, self.vehicle.capacity)
        self.assertEqual(100.5, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_without_enough_fuel_raises_and_dont_change_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(10)
        self.assertEqual(10.5, self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel_subs_the_fuel_and_dont_change_the_capacity(self):
        self.assertEqual(10.5, self.vehicle.fuel)
        self.assertEqual(10.5, self.vehicle.capacity)
        self.vehicle.drive(5)
        self.assertEqual(4.25, self.vehicle.fuel)
        self.assertEqual(10.5, self.vehicle.capacity)

    def test_refuel_method_with_more_than_capacity_fuel_raises_and_not_change_the_fuel(self):
        self.assertEqual(10.5, self.vehicle.fuel)
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual(10.5, self.vehicle.fuel)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_method_with_amount_that_is_not_more_than_capacity(self):
        self.assertEqual(10.5, self.vehicle.fuel)
        self.vehicle.drive(5)
        self.assertEqual(4.25, self.vehicle.fuel)
        self.vehicle.refuel(6.25)
        self.assertEqual(10.5, self.vehicle.fuel)

#   def test_refueling_with_minus_number(self):
#       Test case where I found a bug in the test.
#       self.assertEqual(10.5, self.vehicle.fuel)
#       with self.assertRaises(Exception) as ex:
#            self.vehicle.refuel(-5)
#       self.assertEqual(10.5, self.vehicle.fuel)

    def test_string_representation_works_correctly(self):
        expected_return_message = "The vehicle has 100.5 horse power with 10.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected_return_message, self.vehicle.__str__())


if __name__ == '__main__':
    main()
