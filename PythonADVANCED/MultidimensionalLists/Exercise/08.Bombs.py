def index_validator(numb_rows_cols,r,c):
    return 0 <= r < numb_rows_cols and 0 <= c < numb_rows_cols


def bomb_explosion_near_cells(matr, curr_row, curr_col):
    row_movement = [0, 0, 1, 1, 1, -1, -1, -1]
    col_movement = [1, -1, 0, 1, -1, 0, -1, 1]
    explosion_power = matr[curr_row][curr_col]
    if explosion_power <= 0:
        return matr
    matr[curr_row][curr_col] = 0
    for index in range(len(row_movement)):
        if index_validator(len(matr), curr_row + row_movement[index], curr_col + col_movement[index])\
                and matr[curr_row + row_movement[index]][curr_col + col_movement[index]] > 0:
            matr[curr_row + row_movement[index]][curr_col + col_movement[index]] -= explosion_power
    return matr


rows_cols = int(input())
matrix = [[int(num) for num in input().split()] for row in range(rows_cols)]
indexes = input().split()

for indx in indexes:
    row, col = [int(num) for num in indx.split(',')]
    if not index_validator(rows_cols, row, col):
        continue
    matrix = bomb_explosion_near_cells(matrix, row, col)

alive_cells = [matrix[row][col] for row in range(len(matrix)) for col in range(len(matrix[row])) if matrix[row][col] >0]
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*row, sep=' ') for row in matrix]




