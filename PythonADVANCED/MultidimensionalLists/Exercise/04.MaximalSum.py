rows,cols = [int(num) for num in input().split()]
matrix = [[int(num) for num in input().split()] for row in range(rows)]

largest_sum = 0
largest_list = []
for row in range(0,rows-2):
    for col in range(0,cols - 2):
        primary_digit = matrix[row][col]
        first_next_to_primary = matrix[row][col+1]
        second_next_to_primary = matrix[row][col+2]
        first_above = matrix[row+1][col]
        second_above = matrix[row+1][col+1]
        third_above = matrix[row+1][col+2]
        third_line_above_first = matrix[row+2][col]
        third_line_above_second = matrix[row+2][col+1]
        third_line_above_third = matrix[row+2][col+2]

        total_sum = primary_digit + first_next_to_primary + second_next_to_primary + first_above + second_above + third_above+\
            third_line_above_first + third_line_above_second + third_line_above_third
        current_list = [[primary_digit,first_next_to_primary,second_next_to_primary],\
                        [first_above,second_above,third_above],\
                        [third_line_above_first,third_line_above_second,third_line_above_third]]
        if total_sum >= largest_sum:
            largest_sum = total_sum
            largest_list = current_list

print(f"Sum = {largest_sum}")

for row in largest_list:
    row = [str(num) for num in row]
    print(' '.join(row))