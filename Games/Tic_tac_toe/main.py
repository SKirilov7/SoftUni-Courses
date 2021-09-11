from Tic_tac_toe import core_workshop


def setup():
    first_player = input("Player One,please enter your name:")
    second_player = input("Player Two,please enter your name:")
    first_player_sign = input("Player One,please choose a sign between X and O:").upper().strip()
    second_player_sign = 'X' if first_player_sign == 'O' else 'O'
    dict_of_players = {'First_player_name':first_player, first_player:first_player_sign,
                       'Second_player_name':second_player,second_player:second_player_sign}
    print("This is the numeration of the board: ")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")
    print(f"{first_player} starts first.")
    core_workshop.play(dict_of_players)




if __name__ == '__main__':
    setup()

