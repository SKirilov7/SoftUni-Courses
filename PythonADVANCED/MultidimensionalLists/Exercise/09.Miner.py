def matrix_creator_and_find_miner(row_col):
    matr = []
    miner_pos = None
    num_coals = 0
    for row in range(row_col):
        current_col = input().split()
        matr.append(current_col)
        if 's' in current_col:
            miner_pos = [row,current_col.index('s')]
        if 'c' in current_col:
            num_coals += current_col.count('c')
    return matr,miner_pos,num_coals


def is_valid_position(num_rows_cols,r,c):
    if 0 <= r < num_rows_cols and 0 <= c < num_rows_cols:
        return True
    return False


movement_operator = {
    'left': [0,-1],
    'right': [0, 1],
    'up': [-1, 0],
    'down': [+1, 0]
}


rows_cols = int(input())
commands = input().split()
matrix,miner_position,number_coals = matrix_creator_and_find_miner(rows_cols)

coals_obtained = 0
for command in commands:
    row_to_move,col_to_move = movement_operator[command]
    new_row = miner_position[0] + row_to_move
    new_col = miner_position[1] + col_to_move
    if is_valid_position(rows_cols, new_row, new_col):
        if matrix[new_row][new_col] == 'e':
            print(f"Game over! ({new_row}, {new_col})")
            exit(0)
        if matrix[new_row][new_col] == 'c':
            coals_obtained += 1
        matrix[new_row][new_col] = 's'
        matrix[miner_position[0]][miner_position[1]] = '*'
        miner_position = [new_row, new_col]

    if coals_obtained == number_coals:
        print(f"You collected all coal! ({new_row}, {new_col})")
        exit(0)

print(f"{number_coals - coals_obtained} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")
