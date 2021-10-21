def create_matrix_and_find_player(row_col):
    matrx, p_row, p_col = [], 0, 0
    for row in range(row_col):
        current_col = list(input())
        matrx.append(current_col)
        if 'P' in current_col:
            p_row, p_col = row, current_col.index('P')
    return matrx, p_row, p_col


def is_valid_indexes(r, c, row_col):
    return 0 <= r < row_col and 0 <= c < row_col


direction_mapper = {
    'right': (0, 1),
    'left': (0, -1),
    'up': (-1, 0),
    'down': (1, 0)
}

initial_string = input()
rows_cols = int(input())
matrix, player_row, player_col = create_matrix_and_find_player(rows_cols)
number_commands = int(input())

for _ in range(number_commands):
    command = input()
    next_row, next_col = player_row + direction_mapper[command][0], player_col + direction_mapper[command][1]
    if not is_valid_indexes(next_row, next_col, rows_cols) and initial_string:
        initial_string = initial_string[:-1]
        continue

    if matrix[next_row][next_col].isalpha():
        initial_string += matrix[next_row][next_col]

    matrix[player_row][player_col], matrix[next_row][next_col] = '-', 'P'
    player_row, player_col = next_row, next_col

print(initial_string)
[print(*row, sep='') for row in matrix]
