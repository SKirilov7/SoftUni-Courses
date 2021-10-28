class Owl(Bird):

    def make_sound(self):
        return f"Hoot Hoot"

    def feed(self, food):
        if not food.__class__.__name__ == 'Meat':
            return self.return_message(food)
        self.gain_weight(0.25, food.quantity)


class Hen(Bird):
    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.gain_weight(0.35, food.quantity)
