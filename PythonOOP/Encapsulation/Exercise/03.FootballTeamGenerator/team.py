from project.player import Player


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        if player not in self.__players:
            self.__players.append(player)
            return f"Player {player.name} joined team {self.__name}"
        return f"Player {player.name} has already joined"

    def remove_player(self, player_name: str):
        try:
            searched_player = [player for player in self.__players if player_name == player.name][0]
            self.__players.remove(searched_player)
            return searched_player
        except IndexError:
            return f"Player {player_name} not found"
