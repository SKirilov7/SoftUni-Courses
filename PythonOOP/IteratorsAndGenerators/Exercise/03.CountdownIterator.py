class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.start = self.count

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration
        temp = self.start
        self.start -= 1
        return temp


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
