from unittest import TestCase, main
from StructureAndFunctionality.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self):
        self.paint_factory = PaintFactory('Factory', 10)

    def test_if_init_attaches_correctly(self):
        self.assertEqual('Factory', self.paint_factory.name)
        self.assertEqual(10, self.paint_factory.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)
        self.assertEqual({}, self.paint_factory.ingredients)

    def test_product_getter_returns_correctly(self):
        result = self.paint_factory.products
        self.assertEqual({}, result)

    def test_add_ingredient_with_invalid_product_type(self):
        self.assertEqual({}, self.paint_factory.ingredients)
        with self.assertRaises(TypeError) as ex:
            self.paint_factory.add_ingredient('Black', 10)
        self.assertEqual({}, self.paint_factory.ingredients)
        self.assertEqual("Ingredient of type Black not allowed in PaintFactory", str(ex.exception))

    def test_add_ingredient_with_more_than_capacity(self):
        self.assertEqual({}, self.paint_factory.ingredients)
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.add_ingredient('white', 15)
        self.assertEqual({}, self.paint_factory.ingredients)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_ingredient_works_correctly_and_adds_with_non_existing_type(self):
        self.assertEqual({}, self.paint_factory.ingredients)
        self.paint_factory.add_ingredient('white', 5)
        self.assertEqual({'white': 5}, self.paint_factory.ingredients)

    def test_add_ingredient_works_correctly_with_existing_type(self):
        self.paint_factory.ingredients = {'white': 5}
        self.paint_factory.add_ingredient('white', 5)
        self.assertEqual({'white': 10}, self.paint_factory.ingredients)

    def test_remove_ingredient_with_non_existing_raises(self):
        self.assertEqual({}, self.paint_factory.ingredients)
        with self.assertRaises(KeyError) as ex:
            self.paint_factory.remove_ingredient('white', 1)
        # maybe remove the '
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_remove_ingredient_with_more_than_available(self):
        self.paint_factory.ingredients = {'white': 5}
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.remove_ingredient('white', 7)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_ingredient_with_available_amount(self):
        self.paint_factory.ingredients = {'white': 5}
        self.paint_factory.remove_ingredient('white', 3)
        self.assertEqual({'white': 2}, self.paint_factory.ingredients)

    def test_represent_method(self):
        self.paint_factory.ingredients = {'white': 5}
        expected = "Factory name: Factory with capacity 10.\n" \
                   "white: 5\n"
        result = repr(self.paint_factory)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()