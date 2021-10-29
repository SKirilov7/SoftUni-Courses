from project.animals.animal import Mammal


class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if not self.is_appropriate_food(food):
            return self.return_error_wrong_food(food)
        self.gain_weight(food, 0.10)


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if not self.is_appropriate_food(food):
            return self.return_error_wrong_food(food)
        self.gain_weight(food, 0.40)


class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if not self.is_appropriate_food(food):
            return self.return_error_wrong_food(food)
        self.gain_weight(food, 0.30)


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if not self.is_appropriate_food(food):
            return self.return_error_wrong_food(food)
        self.gain_weight(food, 1)
