class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current_count_returned = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_count_returned == self.count:
            raise StopIteration
        temp = self.current_count_returned
        self.current_count_returned += 1
        return self.step * temp


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
