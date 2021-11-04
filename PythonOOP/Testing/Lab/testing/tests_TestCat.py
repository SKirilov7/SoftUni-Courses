from unittest import TestCase, main
from TestCat import Cat


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat('Gosho')

    def test_if_init_works_properly(self):
        self.assertEqual('Gosho', self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_is_cat_size_increased_after_eating(self):
        self.assertEqual(0, self.cat.size)
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_is_cat_fed_after_eating(self):
        self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_is_cat_sleepy_after_eating(self):
        self.assertFalse(self.cat.sleepy)
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)

    def test_after_eating_cat_cannot_eat_again(self):
        self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_can_cat_fall_asleep_if_not_fed(self):
        self.assertFalse(self.cat.fed)
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_if_cat_is_sleepy_after_sleeping(self):
        self.assertFalse(self.cat.sleepy)
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()
