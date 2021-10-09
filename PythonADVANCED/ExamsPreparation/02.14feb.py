def create_matrix_and_find_player(row_col):
    matrix = []
    plr_row, plr_col = 0, 0
    for row in range(row_col):
        current_col = input().split()
        matrix.append(current_col)
        if 'P' in current_col:
            plr_row, plr_col = row, current_col.index('P')
    return matrix, plr_row, plr_col


def is_valid_move(row_col, r, c):
    return 0 <= r < row_col and 0 <= c < row_col


operation_mapper = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

rows_cols = int(input())
field, player_row, player_col = create_matrix_and_find_player(rows_cols)

coins_obtained = 0
path_of_player = []
while True:
    command = input()
    if command not in operation_mapper:
        continue

    wanted_move_row, wanted_move_col = player_row + operation_mapper[command][0], player_col + operation_mapper[command][1]
    if not is_valid_move(rows_cols, wanted_move_row, wanted_move_col) or field[wanted_move_row][wanted_move_col] == 'X':
        coins_obtained = coins_obtained // 2
        break

    coins_obtained += int(field[wanted_move_row][wanted_move_col])
    path_of_player.append([wanted_move_row, wanted_move_col])
    if coins_obtained >= 100:
        break

    player_row, player_col = wanted_move_row, wanted_move_col

if coins_obtained >= 100:
    print(f"You won! You've collected {coins_obtained} coins.")
else:
    print(f"Game over! You've collected {coins_obtained} coins.")

print(f"Your path: ")
[print(row) for row in path_of_player]




