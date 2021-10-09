def is_valid_indexes(row_col, r, c):
    return 0 <= r < row_col and 0 <= c < row_col


def summing_numbers(field, row, col):
    return (int(field[row][0]) + int(field[row][-1]) + int(field[0][col]) +
                       int(field[-1][col]))


first_player, second_player = input().split(', ')
points = {first_player: [501, 0], second_player: [501, 0]}
row_cols = 7
matrix = [input().split() for row in range(row_cols)]

current_player = first_player
while True:
    throwing_row,throwing_col = [int(num) for num in input()[1:-1].split(', ')]
    points[current_player][1] += 1

    if not is_valid_indexes(row_cols, throwing_row, throwing_col):
        current_player = first_player if current_player == second_player else second_player
        continue

    if matrix[throwing_row][throwing_col] == 'B':
        break

    elif matrix[throwing_row][throwing_col].isdigit():
        points[current_player][0] -= int(matrix[throwing_row][throwing_col])

    elif matrix[throwing_row][throwing_col] == 'D' or matrix[throwing_row][throwing_col] == 'T':
        sum_numbers = summing_numbers(matrix, throwing_row, throwing_col)
        sum_numbers *= 2 if matrix[throwing_row][throwing_col] == 'D' else 3
        points[current_player][0] -= sum_numbers

    if points[current_player][0] <= 0:
        break

    current_player = first_player if current_player == second_player else second_player

print(f'{current_player} won the game with {points[current_player][1]} throws!')