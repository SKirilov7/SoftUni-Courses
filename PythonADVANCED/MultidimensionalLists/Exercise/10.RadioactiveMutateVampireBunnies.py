def matrix_generator_and_player_index_founder(r,c):
    matrix = []
    player_pos = None
    for curr_row in range(r):
        curr_coll = list(input())
        matrix.append(curr_coll)
        if 'P' in curr_coll:
            player_pos = [curr_row, curr_coll.index('P')]
    return matrix,player_pos


def index_validator(rows,cols,curr_r,curr_c):
    if 0 <= curr_r < rows and 0 <= curr_c < cols:
        return True
    return False


def bunny_finder(matrix):
    bunny_found = []
    for curr_row in range(len(matrix)):
        for curr_col in range(len(matrix[curr_row])):
            if matrix[curr_row][curr_col] == 'B':
                bunny_found.append([curr_row,curr_col])

    return bunny_found


def bunny_expander(matrix,bunny_found):
    is_killed = False
    for bunny_row,bunny_col in bunny_found:
        for direction,movement_indexes in movement_operator.items():
            new_r = bunny_row + movement_indexes[0]
            new_c = bunny_col + movement_indexes[1]
            if index_validator(len(matrix), len(matrix[bunny_row]),new_r, new_c):
                if matrix[new_r][new_c] == 'P':
                    is_killed = True
                matrix[new_r][new_c] = 'B'
    return matrix, is_killed


movement_operator = {
    'L': [0, -1],
    'R': [0, 1],
    'U': [-1, 0],
    'D': [1, 0]
}


row, col = [int(num) for num in input().split()]
field, player_position = matrix_generator_and_player_index_founder(row,col)
commands = list(input())

is_dead = False
is_won = False
for command in commands:
    row_ind_to_add, col_ind_to_add = movement_operator[command]
    new_row = player_position[0] + row_ind_to_add
    new_col = player_position[1] + col_ind_to_add
    if index_validator(row, col, new_row, new_col) and field[new_row][new_col] == 'B':
        is_dead = True
        player_position = [new_row, new_col]
    elif index_validator(row, col, new_row, new_col) and not field[new_row][new_col] == 'B':
        field[player_position[0]][player_position[1]] = '.'
        field[new_row][new_col] = 'P'
        player_position = [new_row, new_col]
    else:
        field[player_position[0]][player_position[1]] = '.'
        is_won = True

    bunnies_found = bunny_finder(field)
    field, is_dead = bunny_expander(field,bunnies_found)

    if is_won or is_dead:
        break

[print(''.join(r)) for r in field]
[print(f"won: {player_position[0]} {player_position[1]}") if is_won else print(f"dead: {player_position[0]} {player_position[1]}")]









