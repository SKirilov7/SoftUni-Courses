class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)

    def find_by_type(self, decoration_type: str):
        try:
            return [decoration for decoration in self.decorations if decoration_type == decoration.__class__.__name__][0]
        except IndexError:
            return "None"

