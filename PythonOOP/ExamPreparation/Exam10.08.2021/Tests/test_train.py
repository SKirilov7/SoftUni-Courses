from unittest import TestCase, main

from asdsadasda.train.train import Train


class TestTrain(TestCase):
    def setUp(self):
        self.train = Train('Train', 2)

    def test_if_init_attaches_correctly(self):
        self.assertEqual('Train', self.train.name)
        self.assertEqual(2, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_with_max_passengers(self):
        self.train.passengers = ['Slavi', 'Pesho']
        with self.assertRaises(ValueError) as ex:
            self.train.add('Kiro')
        self.assertEqual(['Slavi', 'Pesho'], self.train.passengers)
        self.assertEqual("Train is full", str(ex.exception))

    def test_add_method_with_existing_passenger(self):
        self.train.passengers = ['Slavi']
        with self.assertRaises(ValueError) as ex:
            self.train.add('Slavi')
        self.assertEqual("Passenger Slavi Exists", str(ex.exception))

    def test_add_method_if_adds(self):
        self.assertEqual([], self.train.passengers)
        return_message = self.train.add('Slavi')
        self.assertEqual(['Slavi'], self.train.passengers)
        self.assertEqual("Added passenger Slavi", return_message)

    def test_remove_with_non_existing_passenger(self):
        self.assertEqual([], self.train.passengers)
        with self.assertRaises(ValueError) as ex:
            self.train.remove('Slavi')
        self.assertEqual("Passenger Not Found", str(ex.exception))

    def test_remove_with_existing_passenger(self):
        self.train.passengers = ['Slavi']
        return_message = self.train.remove('Slavi')
        self.assertEqual([], self.train.passengers)
        self.assertEqual("Removed Slavi", return_message)


if __name__ == '__main__':
    main()
