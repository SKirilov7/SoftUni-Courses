rows,cols = [int(num) for num in input().split()]
matrix = [input().split() for row in range(rows)]

identical_squares = 0
for row in range(0, rows-1):
    for col in range(0, cols-1):
        main_char = matrix[row][col]
        right_side_char = matrix[row][col+1]
        upper_side_char = matrix[row+1][col]
        upper_side_to_right_char = matrix[row+1][col+1]

        if main_char == right_side_char == upper_side_char == upper_side_to_right_char:
            identical_squares += 1

print(identical_squares)