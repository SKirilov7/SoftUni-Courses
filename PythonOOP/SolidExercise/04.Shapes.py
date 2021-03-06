from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, side, h):
        self.side = side
        self.h = h

    def calculate_area(self):
        return (self.side * self.h) / 2


class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_area()

        return total

    def add_shape(self, shape):
        self.shapes.append(shape)

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        if not isinstance(value, list):
            raise TypeError("Should be of type list")

        if 'Shape' not in [sh.__name__ for shape in value for sh in shape.__class__.__mro__]:
            raise TypeError("All elements must be of type Shape")
        self.__shapes = value


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)

calculator.add_shape(Triangle(100, 3))

print(calculator.total_area)

shapes = [Rectangle(1, 6), Triangle(2, 3), Circle(6)]
calculator = AreaCalculator(shapes)
print(calculator.total_area)
