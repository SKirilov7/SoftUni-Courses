def index_validator(row_col, r,c):
    if 0 <= r < row_col and 0 <= c < row_col:
        return True
    return False


rows_cols = int(input())
matrix = [[int(num) for num in input().split()] for r in range(rows_cols)]

command = input()
while not command == 'END':
    command_name, *values = command.split()
    row,col,value_to_insert = [int(num) for num in values]

    if not index_validator(rows_cols,row,col):
        print("Invalid coordinates")
        command = input()
        continue
    if command_name == 'Add':
        matrix[row][col] += value_to_insert
    elif command_name == 'Subtract':
        matrix[row][col] -= value_to_insert

    command = input()

[print(' '.join(str(num) for num in r )) for r in matrix]

