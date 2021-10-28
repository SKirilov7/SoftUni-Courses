from project.animal import Animal


class Cat(Animal):
    def make_sound(self):
        return 'Meow meow!'

    def __repr__(self):
        return self.return_repr_message()


