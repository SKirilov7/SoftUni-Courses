from project.pet_shop import PetShop
from unittest import TestCase, main


class TestPetShop(TestCase):
    def setUp(self) -> None:
        self.petshop = PetShop('Petshop')

    def test_init_attaches_correctly(self):
        self.assertEqual('Petshop', self.petshop.name)
        self.assertEqual({}, self.petshop.food)
        self.assertEqual([], self.petshop.pets)

    def test_add_quantity_with_less_or_equal_to_zero_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.petshop.add_food('food', 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))
        with self.assertRaises(ValueError) as ex2:
            self.petshop.add_food('food', -1)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex2.exception))

    def test_add_food_full_valid_functionality(self):
        self.assertEqual({}, self.petshop.food)
        result = self.petshop.add_food('Food', 10)
        self.assertEqual("Successfully added 10.00 grams of Food.", result)
        self.assertEqual({'Food': 10}, self.petshop.food)
        second_res = self.petshop.add_food('Food', 10)
        self.assertEqual("Successfully added 10.00 grams of Food.", second_res)
        self.assertEqual({'Food': 20}, self.petshop.food)

    def test_add_pet_full_functionality(self):
        self.assertEqual([], self.petshop.pets)
        result = self.petshop.add_pet('Pesho')
        self.assertEqual(['Pesho'], self.petshop.pets)
        self.assertEqual("Successfully added Pesho.", result)
        with self.assertRaises(Exception) as ex:
            self.petshop.add_pet('Pesho')
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_with_non_existing_pet_name(self):
        self.assertEqual([], self.petshop.pets)
        self.petshop.food = {'Food': 10}
        with self.assertRaises(Exception) as ex:
            self.petshop.feed_pet('Food', 'Pesho')
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_with_non_existing_food(self):
        self.petshop.add_pet('Pesho')
        self.assertEqual({}, self.petshop.food)
        result = self.petshop.feed_pet('Food', 'Pesho')
        self.assertEqual('You do not have Food', result)

    def test_feed_pet_with_less_than_100_food(self):
        self.petshop.add_food('Food', 99)
        self.petshop.add_pet('Pesho')
        return_message = self.petshop.feed_pet('Food', 'Pesho')
        self.assertEqual({'Food': 1099}, self.petshop.food)
        self.assertEqual('Adding food...', return_message)

    def test_feed_pet_successfully(self):
        self.petshop.add_pet('Pesho')
        self.petshop.add_food('Food', 1500)
        return_message = self.petshop.feed_pet('Food', 'Pesho')
        self.assertEqual({'Food': 1400}, self.petshop.food)
        self.assertEqual('Pesho was successfully fed', return_message)

    def test_represent_method(self):
        self.petshop.add_pet('Pesho')
        self.petshop.add_pet('Gosho')
        expected = 'Shop Petshop:\nPets: Pesho, Gosho'
        result = repr(self.petshop)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()
