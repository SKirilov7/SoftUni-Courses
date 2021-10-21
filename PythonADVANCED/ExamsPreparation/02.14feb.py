def create_matrix_and_find_player(row_col):
    matrx, p_row, p_col = [], 0, 0
    for row in range(row_col):
        current_col = input().split()
        matrx.append(current_col)
        if 'P' in current_col:
            p_row, p_col = row, current_col.index('P')
    return matrx, p_row, p_col


def is_valid_indexes(r, c, row_col):
    return 0 <= r < row_col and 0 <= c < row_col


movement_operator = {
    'right': (0, 1),
    'left': (0, -1),
    'up': (-1, 0),
    'down': (1, 0)
}

rows_cols = int(input())
matrix, player_row, player_col = create_matrix_and_find_player(rows_cols)

coins_collected = 0
movements = []

while True:
    command = input()
    if not command in movement_operator:
        continue
    next_row, next_col = player_row + movement_operator[command][0], player_col + movement_operator[command][1]

    if not is_valid_indexes(next_row, next_col, rows_cols) or matrix[next_row][next_col] == 'X':
        coins_collected //= 2
        break

    coins_collected += int(matrix[next_row][next_col])
    movements.append([next_row, next_col])
    matrix[player_row][player_col], matrix[next_row][next_col] = 0, 'P'
    player_row, player_col = next_row, next_col

    if coins_collected >= 100:
        break


print(f"You won! You've collected {coins_collected} coins.") if coins_collected >= 100 \
    else print(f"Game over! You've collected {coins_collected} coins.")
print('Your path:')
[print(indexes) for indexes in movements]
