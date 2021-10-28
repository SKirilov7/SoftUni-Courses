class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f'{self.name} {self.surname}'

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __repr__(self):
        return f"Group {self.name} with members {', '.join([member.__repr__() for member in self.people])}"

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        return Group(f'{self.name} {other.name}', self.people + other.people)

    def __getitem__(self, index):
        return [f'Person {index}: {member}' for member in self.people if self.people.index(member) == index][0]