from project.animal import Animal


class Dog(Animal):
    def make_sound(self):
        return "Woof!"

    def __repr__(self):
        return self.return_repr_message()
