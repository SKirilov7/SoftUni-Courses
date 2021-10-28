class Mouse(Mammal):

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if not food.__class__.__name__ == 'Fruit' and not food.__class__.__name__ == 'Vegetable':
            return self.return_message(food)
        self.gain_weight(0.10, food.quantity)


class Dog(Mammal):

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if not food.__class__.__name__ == 'Meat':
            return self.return_message(food)
        self.gain_weight(0.40, food.quantity)


class Cat(Mammal):

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if not food.__class__.__name__ == 'Meat' and not food.__class__.__name__ == 'Vegetable':
            return self.return_message(food)
        self.gain_weight(0.30, food.quantity)


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if not food.__class__.__name__ == 'Meat':
            return self.return_message(food)
        self.gain_weight(1, food.quantity)


