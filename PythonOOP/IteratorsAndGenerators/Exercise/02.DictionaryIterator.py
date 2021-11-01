class dictionary_iter:
    def __init__(self, dictionary):
        self.tuples_of_elements = list(dictionary.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.tuples_of_elements):
            raise StopIteration
        temp = self.index
        self.index += 1
        return self.tuples_of_elements[temp]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
