def create_matrix_and_find_snake_and_burrows(row_col):
    matrix, s_row, s_col = [], 0, 0
    for row in range(row_col):
        current_col = list(input())
        matrix.append(current_col)
        if 'S' in current_col:
            s_row, s_col = row, current_col.index('S')
    return matrix, s_row, s_col,


def is_valid_indexes(r, c, row_col):
    return 0 <= r < row_col and 0 <= c < row_col


movement_operator = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0)
}

rows_cols = int(input())
matrix, snake_row, snake_col = create_matrix_and_find_snake_and_burrows(rows_cols)

food_eaten = 0
while True:
    command = input()
    next_row, next_col = snake_row + movement_operator[command][0], snake_col + movement_operator[command][1]
    matrix[snake_row][snake_col] = '.'
    if not is_valid_indexes(next_row, next_col, rows_cols):
        break

    if matrix[next_row][next_col] == 'B':
        matrix[next_row][next_col] = '.'
        next_row, next_col = [[row, col] for row in range(len(matrix)) for col in range(len(matrix[row])) if matrix[row][col] == 'B'][0]
    elif matrix[next_row][next_col] == '*':
        food_eaten += 1

    matrix[next_row][next_col] = 'S'
    snake_row, snake_col = next_row, next_col

    if food_eaten >= 10:
        break

print(f"You won! You fed the snake.") if food_eaten >= 10 else print('Game over!')
print(f"Food eaten: {food_eaten}")
[print(*row, sep='') for row in matrix]
