from copy import deepcopy


class HashTable:
    def __init__(self):
        self.max_capacity = 4
        self.__keys = [None] * self.max_capacity
        self.__values = [None] * self.max_capacity

    @property
    def length(self):
        return self.max_capacity

    def find_available_index(self, index):
        if index == self.max_capacity:
            return self.find_available_index(0)
        if self.__keys[index] is None:
            return index
        return self.find_available_index(index + 1)

    def resize(self):
        self.__keys += [None] * self.max_capacity
        self.__values += [None] * self.max_capacity
        self.max_capacity *= 2

    def hash(self, key):
        index = sum([ord(char) for char in key]) % self.max_capacity
        available_index = self.find_available_index(index)
        return available_index

    def add(self, key, value):
        self.__setitem__(key, value)

    def get(self, key, default=None):
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def __getitem__(self, item):
        try:
            index = self.__keys.index(item)
            return self.__values[index]
        except ValueError:
            raise KeyError("Key is not in dict")

    def __setitem__(self, key, value):
        if key in self.__keys:
            index = self.__keys.index(key)
            self.__values[index] = value
            return

        if len([key for key in self.__keys if key is not None]) == self.max_capacity:
            self.resize()

        index = self.hash(key)
        self.__keys[index] = key
        self.__values[index] = value

    def __repr__(self):
        result = '{' + ', '.join([f"{self.__keys[index]}: {self.__values[index]}"
                                  for index in range(len(self.__keys)) if not self.__keys[index] is None]) + '}'
        return result

    def __len__(self):
        return len([key for key in self.__keys if key is not None])

    def keys(self):
        return [key for key in self.__keys if key is not None]

    def values(self):
        values = []
        for key in self.keys():
            index = self.__keys.index(key)
            values.append(self.__values[index])
        return values

    def copy(self):
        return deepcopy(self)

    def items(self):
        return list(zip(self.keys(), self.values()))

    def pop(self, key):
        try:
            index = self.__keys.index(key)
            self.__keys[index] = None
            value_to_return = self.__values[index]
            self.__values[index] = None
            return value_to_return
        except ValueError:
            raise KeyError('Invalid key')

    def clear(self):
        self.max_capacity = 4
        self.__keys = [None] * self.max_capacity
        self.__values = [None] * self.max_capacity


table = HashTable()

table["name"] = "Pesho"
table["age"] = 25
print(table)
print(table.get("name"))
print(table["age"])
print(len(table))
print(table.length)
print(table.keys())
print(table.values())
print(table.items())
a = table.copy()
a["name"] = 6
print(table["name"])
table.add("fromtest", 5)
print(table)
