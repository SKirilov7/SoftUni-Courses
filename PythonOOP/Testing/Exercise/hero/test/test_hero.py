from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.main_hero = Hero('Pesho', 10, 100, 10)
        self.enemy_hero = Hero('Ivan', 10, 80, 20)

    def test_if_init_adds_instance_attributes_correctly(self):
        self.assertEqual('Pesho', self.main_hero.username)
        self.assertEqual(10, self.main_hero.level)
        self.assertEqual(100, self.main_hero.health)
        self.assertEqual(10, self.main_hero.damage)

    def test_if_battle_with_the_same_hero_raises(self):
        second_hero = Hero('Pesho', 10, 100, 10)
        with self.assertRaises(Exception) as ex:
            self.main_hero.battle(second_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_if_main_hero_cannot_battle_with_zero_health(self):
        self.main_hero.health = 0
        self.assertTrue(self.enemy_hero.health > 0)
        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_if_enemy_hero_cannot_battle_with_zero_health(self):
        self.enemy_hero.health = 0
        self.assertTrue(self.main_hero.health > 0)
        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight Ivan. He needs to rest", str(ex.exception))

    def test_if_draw_works_correctly_with_both_zero_health(self):
        self.main_hero.health = 200
        self.enemy_hero.health = 100
        return_message = self.main_hero.battle(self.enemy_hero)
        self.assertEqual(0, self.main_hero.health)
        self.assertEqual(0, self.enemy_hero.health)
        self.assertEqual("Draw", return_message)

    def test_if_draw_works_with_both_hero_under_zero_health(self):
        return_message = self.main_hero.battle(self.enemy_hero)
        self.assertTrue(self.main_hero.health < 0)
        self.assertTrue(self.enemy_hero.health < 0)
        self.assertEqual("Draw", return_message)

    def test_if_enemy_player_health_goes_under_makes_main_hero_win_and_upgrade(self):
        self.main_hero.health = 300
        return_message = self.main_hero.battle(self.enemy_hero)
        self.assertTrue(self.enemy_hero.health < 0)
        self.assertEqual(105, self.main_hero.health)
        self.assertEqual(11, self.main_hero.level)
        self.assertEqual(15, self.main_hero.damage)
        self.assertEqual("You win", return_message)

    def test_if_main_hero_health_goes_under_makes_enemy_hero_win_and_upgrade(self):
        self.enemy_hero.health = 120
        return_message = self.main_hero.battle(self.enemy_hero)
        self.assertTrue(self.main_hero.health < 0)
        self.assertEqual(25, self.enemy_hero.health)
        self.assertEqual(11, self.enemy_hero.level)
        self.assertEqual(25, self.enemy_hero.damage)
        self.assertEqual('You lose', return_message)

    def test_str_representation_works_correctly(self):
        expected_return_message = "Hero Pesho: 10 lvl\nHealth: 100\nDamage: 10\n"
        self.assertEqual(expected_return_message, self.main_hero.__str__())


if __name__ == '__main__':
    main()
