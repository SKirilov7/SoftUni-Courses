import sys
from copy import deepcopy


class CustomList:
    def __init__(self, *args):
        self.__values = list(args)

    def append(self, value):
        if not value or value == ' ':
            raise ValueError('You need to append a valid value.')
        self.__values.append(value)
        return self.__values

    @staticmethod
    def check_if_is_valid_index(index, length_values):
        return index >= length_values or index < 0

    def remove(self, index):
        if CustomList.check_if_is_valid_index(index, len(self.__values)):
            raise IndexError('Index out of range.')
        return self.__values.pop(index)

    def get(self, index):
        if CustomList.check_if_is_valid_index(index, len(self.__values)):
            raise IndexError('Index out of range.')
        return self.__values[index]

    def extend(self, iterable):
        if isinstance(iterable, int) or isinstance(iterable, str):
            self.__values.append(iterable)
            return deepcopy(self.__values)
        self.__values.extend([el for el in iterable])
        return deepcopy(self.__values)

    def insert(self, index, value):
        if CustomList.check_if_is_valid_index(index, len(self.__values)):
            raise IndexError('Index out of range.')
        self.__values.insert(index, value)
        return self.__values

    def pop(self):
        return self.__values.pop()

    def clear(self):
        self.__values = []
        return self.__values

    def index(self, value):
        if value in self.__values:
            return self.__values.index(value)
        raise ValueError('Value is not in list.')

    def count(self, value):
        try:
            return self.__values.count(value)
        except ValueError:
            raise ValueError('Value is not in list.')

    def reverse(self):
        return list(reversed(self.__values))

    def copy(self):
        return deepcopy(self.__values)

    def size(self):
        return len(self.__values)

    def add_first(self, value):
        if len(self.__values) == 0:
            self.__values.append(value)
        else:
            self.__values.insert(0, value)
        return self.__values

    def dictionize(self):
        dict = {}
        for index in range(0, len(self.__values), 2):
            if index == len(self.__values) - 1:
                dict[self.__values[index]] = ' '
                break
            dict[self.__values[index]] = self.__values[index + 1]
        return dict

    def move(self, amount):
        if amount > len(self.__values) - 1:
            raise IndexError('Please add a valid amount.')
        self.__values = self.__values[amount:] + self.__values[:amount]
        return self.__values

    def sum(self):
        total_sum = 0
        for el in self.__values:
            if isinstance(el, int) or isinstance(el, float):
                total_sum += el
                continue
            if isinstance(el, str):
                total_sum += len(el)
            if '__add__' in dir(el):
                amount = el.__add__(5)
                total_sum += amount
            else:
                raise ValueError('Every class in the list must have add method.')
        return total_sum

    def overbound(self):
        max_number = -sys.maxsize
        biggest_num_index = 0
        for index in range(len(self.__values)):
            current_element = self.__values[index]
            if isinstance(current_element, int) or isinstance(current_element, float):
                if current_element > max_number:
                    max_number = current_element
                    biggest_num_index = index
                continue
            if isinstance(current_element, str) and len(current_element) > max_number:
                max_number = len(current_element)
                biggest_num_index = index
            elif '__len__' in dir(current_element):
                if current_element.__len__() > max_number:
                    max_number = current_element.__len__()
                    biggest_num_index = index
            else:
                raise ValueError('Every class in the list must have len method.')
        return biggest_num_index

    def underbound(self):
        min_number = sys.maxsize
        smallest_num_index = 0
        for index in range(len(self.__values)):
            current_element = self.__values[index]
            if isinstance(current_element, int) or isinstance(current_element, float):
                if current_element < min_number:
                    min_number = current_element
                    smallest_num_index = index
                continue
            if isinstance(current_element, str) and len(current_element) < min_number:
                min_number = len(current_element)
                smallest_num_index = index
            elif '__len__' in dir(current_element):
                if current_element.__len__() < min_number:
                    min_number = current_element.__len__()
                    smallest_num_index = index
            else:
                raise ValueError('Every class in the list must have len method.')
        return smallest_num_index


class PersonWithDunders:
    def __add__(self, other):
        return 5

    def __len__(self):
        return 10

    def __repr__(self):
        return f'PersonObject'


class PersonWithoutDunders:
    pass


cl = CustomList(1, 2, 3)
print(cl.append(5))
print(cl.remove(2))
print(cl.get(2))
print(cl.extend(10))
print(cl.extend([11, 12, 13]))
print(cl.insert(6, 100))
print(cl.pop())
print(cl.index(100))
print(cl.insert(6, 100))
print(cl.count(100))
print(cl.reverse())
print(cl.extend(10))
print(cl.size())
print(cl.add_first(1000))
print(cl.add_first(1111))
print(cl.dictionize())
print(cl.size())
print(cl.move(10))
person = PersonWithDunders()
person2 = PersonWithoutDunders()
print(cl.add_first(person))
# print(cl.add_first(person2))
# print(cl.add_first(person2))
print(cl.sum())
print(cl.overbound())
print(cl.underbound())
