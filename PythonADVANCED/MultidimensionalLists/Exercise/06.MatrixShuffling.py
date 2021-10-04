def index_validator(rows,cols,row_1,col_1,row_2,col_2):
    return 0 <= row_1 < rows and 0 <= row_2 < rows and 0 <= col_1 < cols and 0 <= col_2 < cols


rows,cols = [int(num) for num in input().split()]
matrix = [input().split() for row in range(rows)]

command = input()
while not command == 'END':
    try:
        current_command ,*numbers = command.split()
        row_one,col_one,row_two,col_two = [int(num) for num in numbers]
        if not current_command == 'swap' or not index_validator(rows,cols,row_one,col_one,row_two,col_two):
            print('Invalid input!')
            command = input()
            continue

        matrix[row_one][col_one],matrix[row_two][col_two] = matrix[row_two][col_two],matrix[row_one][col_one]

        for row in matrix:
            print(' '.join(row))

    except ValueError:
        print('Invalid input!')

    command = input()