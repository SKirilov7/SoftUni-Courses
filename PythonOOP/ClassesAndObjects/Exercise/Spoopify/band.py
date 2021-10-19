from project.song import Song
from project.album import Album

class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        current_album_to_remove = [a for a in self.albums if a.name == album_name]
        if current_album_to_remove:
            current_album_to_remove = current_album_to_remove[0]
            if current_album_to_remove.published:
                return f"Album has been published. It cannot be removed."
            self.albums.remove(current_album_to_remove)
            return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = f"Band {self.name}\n"
        result += '\n'.join([a.details() for a in self.albums])
        return result




