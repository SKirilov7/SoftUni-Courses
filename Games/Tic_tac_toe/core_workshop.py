from mappers import *
from helpers import *


def print_board(board):
    for row in board:
        print(f"| {' | '.join(row)} |")


def create_board():
    board = [[' ',' ',' '] for row in range(3)]
    return board


def play(dict_players):
    board = create_board()
    counter_choosing = 1
    while True:
        players_mapper = mapper_for_choice(dict_players)
        current_player = players_mapper[counter_choosing % 2]
        current_sign = dict_players[current_player]

        current_player_choosing = int(input(f"{current_player}, please choose a free position(1-9):"))

        if is_valid_choosing(current_player_choosing):
            current_indexes_chosen = is_valid_choosing(current_player_choosing)
            if is_free_space(board, current_indexes_chosen):
                row, col = current_indexes_chosen
                board[row][col] = current_sign
                print_board(board)
                if counter_choosing >= 5:
                    if is_winner(board):
                        print(f"{current_player} won the game")
                        exit(0)
                if counter_choosing == 9:
                    print(f"Game over.All positions are taken.")
                    exit(0)
                counter_choosing += 1
            else:
                continue
        else:
            continue
