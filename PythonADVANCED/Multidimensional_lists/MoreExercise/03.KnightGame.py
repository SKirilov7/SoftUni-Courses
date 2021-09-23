def create_chess_board_and_find_knights(row_col_num):
    matrix = []
    knights = []
    for row in range(row_col_num):
        current_col = list(input())
        for index in range(len(current_col)):
            if current_col[index] == 'K':
                knights.append([row,index])
        matrix.append(current_col)
    return matrix, knights


def is_valid_index(matrix,curr_row,curr_col):
    if 0 <= curr_row < len(matrix) and 0 <= curr_col < len(matrix[curr_row]):
        return True
    return False


def knight_movement_and_kills(matrix,curr_row,curr_col):
    kills = 0
    rows_movement = [-2, -2, -1, -1, 2, 2, 1, 1]
    cols_movement = [-1, 1, -2, 2, -1, 1, -2, 2]
    for index in range(len(rows_movement)):
        new_row = curr_row + rows_movement[index]
        new_col = curr_col + cols_movement[index]
        if is_valid_index(matrix,new_row,new_col):
            if matrix[new_row][new_col] == 'K':
                kills += 1
    return kills


rows_cols = int(input())
chess_board, knight_placement = create_chess_board_and_find_knights(rows_cols)

knights_removed = 0
while True:
    most_kills = 0
    best_killer = None
    for knight_index,knight_column in knight_placement:
        kills_made = knight_movement_and_kills(chess_board, knight_index, knight_column)
        if kills_made > most_kills:
            most_kills = kills_made
            best_killer = [knight_index,knight_column]

    if most_kills == 0:
        break

    chess_board[best_killer[0]][best_killer[1]] = '0'
    knight_placement.remove(best_killer)
    knights_removed += 1


print(knights_removed)


