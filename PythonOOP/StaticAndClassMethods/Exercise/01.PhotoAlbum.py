from math import ceil


class PhotoAlbum:
    max_photo_per_page = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for num in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label:str):
        index_to_add_to_page = 1
        for index in range(len(self.photos)):
            if len(self.photos[index]) < PhotoAlbum.max_photo_per_page:
                self.photos[index].append(label)
                return f"{label} photo added successfully on page {index + index_to_add_to_page} " \
                       f"slot {len(self.photos[index])}"
        return "No more free slots"

    def display(self):
        result = f'-----------\n'
        for page in self.photos:
            if page:
                result += ' '.join('[]' for _ in range(len(page)))
            result += '\n'
            result += f'-----------\n'
        return result





