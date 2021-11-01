class vowels:
    def __init__(self, text):
        self.text = text
        self.start = 0
        self.vowels = 'AEIOUYE'
        self.vowels_in_text = [char for char in self.text if char.upper() in self.vowels]
        self.end = len(self.vowels_in_text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        temp = self.start
        self.start += 1
        return self.vowels_in_text[temp]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
