def create_matrix_and_find_snake(row_col):
    matrix, s_row, s_col = [], 0, 0
    first_burrow = []
    second_burrow = []
    for row in range(row_col):
        current_col = list(input())
        matrix.append(current_col)
        if 'S' in current_col:
            s_row, s_col = row, current_col.index('S')
        if 'B' in current_col:
            if not first_burrow:
                first_burrow = [row, current_col.index('B')]
            elif not second_burrow:
                second_burrow = [row, current_col.index('B')]
    return matrix, s_row, s_col, first_burrow, second_burrow


def movement_operator(r,c,command_data):
    if command_data == 'left':
        c -= 1
    elif command_data == 'right':
        c += 1
    elif command_data == 'up':
        r -= 1
    elif command_data == 'down':
        r += 1
    return r, c


def is_valid_index(row_col, r, c):
    return 0 <= r < row_col and 0 <= c < row_col


rows_cols = int(input())
field, snake_row, snake_col, first_burrow, second_burrow = create_matrix_and_find_snake(rows_cols)

food_eaten = 0
while True:
    command = input()
    next_row, next_col = movement_operator(snake_row, snake_col, command)
    if not is_valid_index(rows_cols, next_row, next_col):
        field[snake_row][snake_col] = '.'
        print('Game over!')
        break

    if field[next_row][next_col] == 'B' and (first_burrow or second_burrow):
        field[snake_row][snake_col] = '.'

    if field[next_row][next_col] == 'B' and [next_row, next_col] == first_burrow:
        field[next_row][next_col] = '.'
        snake_row, snake_col = second_burrow[0], second_burrow[1]
    elif field[next_row][next_col] == 'B' and [next_row, next_col] == second_burrow:
        field[next_row][next_col] = '.'
        snake_row, snake_col = first_burrow[0], first_burrow[1]

    else:
        if field[next_row][next_col] == '*':
            food_eaten += 1
        field[snake_row][snake_col] = '.'
        snake_row, snake_col = next_row, next_col

    field[snake_row][snake_col] = 'S'
    if food_eaten >= 10:
        print(f"You won! You fed the snake.")
        break


print(f"Food eaten: {food_eaten}")
[print(*row,sep='') for row in field]













