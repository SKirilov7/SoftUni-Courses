rows_cols = int(input())

matrix = [[int(num) for num in input().split(' ')] for row in range(rows_cols)]
primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for row_col in range(len(matrix)):
    primary_diagonal_sum += matrix[row_col][row_col]
    secondary_diagonal_sum += matrix[row_col][-1-row_col]

print(abs(primary_diagonal_sum - secondary_diagonal_sum))
