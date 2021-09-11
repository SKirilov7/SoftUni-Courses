from mappers import mapper_for_choice,index_mapper


def is_valid_choosing(number):
    if number in index_mapper:
        return index_mapper[number]
    return False


def is_free_space(board,indexes):
    row,col = indexes
    if board[row][col] == ' ':
        return True
    return False


def is_row_winner(board):
    for row in board:
        if row.count('X') == len(row) or row.count('O') == len(row):
            return True
    return False


def is_column_winner(board):
    first_column = [board[0][0],board[1][0],board[2][0]]
    second_column = [board[0][1],board[1][1],board[2][1]]
    third_column = [board[2][0],board[2][1],board[2][2]]
    if first_column.count('X') == 3 or first_column.count('O') == 3:
        return True
    elif second_column.count('X') == 3 or second_column.count('O') == 3:
        return True
    elif third_column.count('X') == 3 or third_column.count('O') == 3:
        return True
    return False


def is_primary_diagonal_winner(board):
    list = []
    for row in range(len(board)):
        list.append(board[row][row])

    if list.count('X') == 3 or list.count('O') == 3:
        return True
    return False


def is_opposite_diagonal_winner(board):
    n = len(board)
    list = []
    for i in range(len(board)):
        list.append(board[i][n-i-1])
    if list.count('X') == 3 or list.count('O') == 3:
        return True
    return False


def is_winner(board):
    if is_row_winner(board) or is_column_winner(board) or is_primary_diagonal_winner(board) or is_opposite_diagonal_winner(board):
        return True
    return False
