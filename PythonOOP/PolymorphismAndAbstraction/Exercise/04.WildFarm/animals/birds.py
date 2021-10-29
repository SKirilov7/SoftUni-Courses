from project.animals.animal import Bird


class Owl(Bird):
    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if not self.is_appropriate_food(food):
            return self.return_error_wrong_food(food)
        self.gain_weight(food, 0.25)


class Hen(Bird):
    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        if not self.is_appropriate_food(food):
            self.return_error_wrong_food(food)
        self.gain_weight(food, 0.35)
