def create_board(row=6,col=7):
    return [[0] * col for row in range(row)]


def is_valid_column(board,column):
    for row in board:
        if 0 <= column < len(row) and 0 in row:
            return True
        return False


def is_valid_indexes(board,row,col):
    if 0 <= row < len(board):
        if 0 <= col < len(board[row]):
            return True
    return False


def put_the_chosen_symbol(board,column,curr_player):
    row_to_find = 0
    for row in range(len(board)-1,-1,-1):
        if board[row][column] == 0:
            row_to_find = row
            break
    return row_to_find


def is_row_winner(board,player,row,col):
    if 4 * str(player) in ''.join([str(num) for num in board[row]]):
        return True
    return False


def is_column_winner(board,player,row,col):
    try:
        if board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
            return True
    except IndexError:
        return False


def is_primary_diagonal_winner(board,player,row,col):
    starting_row = row
    starting_col = col

    for i in range(4):
        if is_valid_indexes(board,starting_row-1,starting_col-1) and board[starting_row-1][starting_col-1] == player:
            starting_row = starting_row - 1
            starting_col = starting_col - 1
        else:
            break
    try:
        if board[starting_row+1][starting_col+1] == player and board[starting_row+2][starting_col+2] == player\
                and board[starting_row + 3][starting_col + 3] == player:
            return True
    except IndexError:
        return False


def is_other_diagonal_winner(board,player,row,col):
    starting_row = row
    starting_col = col

    for i in range(4):
        if is_valid_indexes(board,starting_row+1,starting_col-1) and board[starting_row+1][starting_col-1] == player:
            starting_row = starting_row + 1
            starting_col = starting_col - 1
        else:
            break

    try:
        if board[starting_row -1][starting_col + 1] == player and board[starting_row - 2][starting_col + 2] == player \
                and board[starting_row - 3][starting_col + 3] == player:
            return True
    except IndexError:
        return False


def is_winner(board,player,row,col):
    if is_row_winner(board,player,row,col) or is_column_winner(board,player,row,col) or\
            is_primary_diagonal_winner(board,player,row,col) or is_other_diagonal_winner(board,player,row,col):
        return True
    return False


def print_board(board):
    for row in board:
        print(row)


def play(board,first_player,second_player):
    current_player = 1
    while True:
        column_chosen=int(input(f"Player {current_player},please choose a column(1-{len(board)}):")) - 1

        if is_valid_column(board,column_chosen):
            row_chosen = put_the_chosen_symbol(board,column_chosen,current_player)
            board[row_chosen][column_chosen] = current_player
            print_board(board)
            if is_winner(board,current_player,row_chosen,column_chosen):
                print(f'Player {current_player} won the game!')
                break

            current_player = 2 if current_player == 1 else 1

        else:
            print('Invalid column,please choose again: ')
            continue


player_one = 1
player_two = 2
board = create_board()

play(board,player_one,player_two)

