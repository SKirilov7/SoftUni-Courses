from project.song import Song


class Album:
    def __init__(self, name, songs=None):
        self.name = name
        self.songs = []
        if songs:
            self.songs.append(songs)
        self.published = False

    def add_song(self, song: Song):
        if song in self.songs:
            return "Song is already in the album."
        if self.published:
            return "Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return f"Cannot remove songs. Album is published."
        try:
            song_to_remove = [s for s in self.songs if s.name == song_name][0]
            self.songs.remove(song_to_remove)
            return f"Removed song {song_name} from album {self.name}."
        except IndexError:
            return f"Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        result = f'Album {self.name}\n'
        result += '\n'.join([f'== {s.name} - {s.length}'for s in self.songs])
        return result



