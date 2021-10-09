def create_matrix_and_find_player(row_col):
    matrix, pl_row, pl_col = [], None, None
    for row in range(row_col):
        current_col = list(input())
        if 'P' in current_col:
            pl_row,pl_col = row, current_col.index('P')
        matrix.append(current_col)
    return matrix, pl_row, pl_col


def is_valid_index(row_col, r, c):
    return 0 <= r < row_col and 0 <= c < row_col


operation_mapper = {
    'left': [0, -1],
    'right': [0, 1],
    'up': [-1, 0],
    'down': [1, 0]
}

string = input()
rows_cols = int(input())
matrix, player_row, player_col = create_matrix_and_find_player(rows_cols)


number_commands = int(input())

for _ in range(number_commands):
    command = input()
    wanted_movement_row = player_row + operation_mapper[command][0]
    wanted_movement_col = player_col + operation_mapper[command][1]

    if not is_valid_index(rows_cols, wanted_movement_row, wanted_movement_col) and string:
        string = string[0:-1]
        continue

    elif is_valid_index(rows_cols, wanted_movement_row, wanted_movement_col) and matrix[wanted_movement_row][wanted_movement_col].isalpha():
        string += matrix[wanted_movement_row][wanted_movement_col]

    matrix[player_row][player_col] = '-'
    matrix[wanted_movement_row][wanted_movement_col] = 'P'
    player_row, player_col = wanted_movement_row, wanted_movement_col

print(string)
[print(*row, sep='') for row in matrix]