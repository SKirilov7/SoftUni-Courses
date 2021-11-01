class sequence_repeat:
    def __init__(self, word, count_chars):
        self.word = word
        self.count_chars = count_chars
        self.index = 0
        self.amount_chars_returned = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.amount_chars_returned == self.count_chars:
            raise StopIteration
        temp = self.index
        self.index += 1
        self.amount_chars_returned += 1
        return self.word[temp % len(self.word)]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
