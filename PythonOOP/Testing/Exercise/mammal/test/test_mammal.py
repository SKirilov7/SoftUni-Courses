from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal('Pesho', 'Pig', 'gruh')

    def test_if_init_sets_attributes_properly(self):
        self.assertEqual('Pesho', self.mammal.name)
        self.assertEqual('Pig', self.mammal.type)
        self.assertEqual('gruh', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound_method_returns_correctly(self):
        self.assertEqual(f"Pesho makes gruh", self.mammal.make_sound())

    def test_info_returns_correctly(self):
        self.assertEqual(f"Pesho is of type Pig", self.mammal._Mammal__kingdom)

    def test_get_kingdom(self):
        self.assertEqual('animals', self.mammal.get_kingdom())


if __name__ == '__main__':
    main()
