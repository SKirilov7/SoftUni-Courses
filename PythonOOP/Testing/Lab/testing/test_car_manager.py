from unittest import TestCase, main
#from CarManager import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car(make='BMW', model=535, fuel_consumption=10, fuel_capacity=70)

    def test_if_init_works_properly(self):
        self.assertEqual('BMW', self.car.make)
        self.assertEqual(535, self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(70, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_if_making_make_none_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_if_making_model_none_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_if_making_fuel_consumption_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_if_making_fuel_capacity_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_if_making_fuel_amount_less_than_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -10

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_if_refueling_with_more_than_zero_fuel_works(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(15)
        self.assertEqual(15, self.car.fuel_amount)

    def test_if_refueling_with_more_than_max_capacity_works(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(150)
        self.assertEqual(70, self.car.fuel_amount)

    def test_if_refueling_with_less_than_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-10)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_if_driving_with_enough_fuel_subs_fuel(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(70)
        self.assertEqual(70, self.car.fuel_amount)
        self.car.drive(10)
        self.assertEqual(69, self.car.fuel_amount)

    def test_if_driving_with_less_fuel_raises(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(5)
        self.assertEqual(5, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == '__main__':
    main()
