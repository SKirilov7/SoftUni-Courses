def around_bomb_numbers(matrix,row,col):
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if is_valid_index(len(matrix), r, c) and not matrix[r][c] == '*':
                matrix[r][c] += 1
    return matrix


def is_valid_index(row_col, r, c):
    return 0 <= r < row_col and 0 <= c < row_col


rows_cols = int(input())
field = [[0] * rows_cols for row in range(rows_cols)]

number_bombs = int(input())
for _ in range(number_bombs):
    bomb_row, bomb_col = [int(num) for num in input()[1:-1].split(', ')]
    field[bomb_row][bomb_col] = '*'
    field = around_bomb_numbers(field, bomb_row, bomb_col)

[print(*row, sep=' ') for row in field]

