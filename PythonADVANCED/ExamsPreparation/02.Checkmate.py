# FIRST solution with USING THE KING as starting point.
def create_matrix_and_find_king(row_col):
    matrix, k_row, k_col = [], 0, 0
    for row in range(row_col):
        current_col = input().split()
        matrix.append(current_col)
        if 'K' in current_col:
            k_row, k_col = row, current_col.index('K')
    return matrix, k_row, k_col


def is_valid_index(r, c, row_col):
    return 0 <= r < row_col and 0 <= c < row_col


rows_cols = 8
matrix, king_row, king_col = create_matrix_and_find_king(rows_cols)

movement_row = [-1, -1, 1, 0, 0, 1, 1, 1]
movement_col = [-1, 0, 1, -1, 1, -1, 0, 1]

queens_capable_of_killing = []
for index in range(len(movement_row)):
    next_row, next_col = king_row + movement_row[index], king_col + movement_col[index]
    while is_valid_index(next_row, next_col, rows_cols):
        if matrix[next_row][next_col] == 'Q':
            queens_capable_of_killing.append([next_row, next_col])
            break
        next_row += movement_row[index]
        next_col += movement_col[index]

print(*queens_capable_of_killing, sep='\n') if queens_capable_of_killing else print('The king is safe!')


# SECOND solution with queens killing the KING.
# def queen_moving(field, q_row, q_col):
#     is_king_killed = False
#     row_steps = [1, -1, -1, 1, 0, 0, -1, 1]
#     col_steps = [1, -1, 1, -1, 1, -1, 0, 0]
#
#     for index in range(len(row_steps)):
#         current_row, current_col = q_row + row_steps[index], q_col + col_steps[index]
#         while is_valid_step(len(field), current_row, current_col):
#             if field[current_row][current_col] == 'K':
#                 is_king_killed = True
#                 break
#             if field[current_row][current_col] == 'Q':
#                 break
#             current_row += row_steps[index]
#             current_col += col_steps[index]
#         if is_king_killed:
#             return True
#     return False
#
#
# def is_valid_step(row_col, r, c):
#     return 0 <= r < row_col and 0 <= c < row_col
#
#
# rows_cols = 8
# chess_board = [input().split() for row in range(rows_cols)]
#
# queens_capable_of_killing = []
# for row in range(rows_cols):
#     for col in range(rows_cols):
#         if chess_board[row][col] == 'Q' and queen_moving(chess_board, row, col):
#             queens_capable_of_killing.append([row, col])
#
# [print(row) for row in reversed(queens_capable_of_killing)] if queens_capable_of_killing else print('The king is safe!')

