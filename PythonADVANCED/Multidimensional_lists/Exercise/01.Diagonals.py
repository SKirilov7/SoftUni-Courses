rows_cols = int(input())

matrix = [[int(num) for num in input().split(', ')] for row in range(rows_cols)]
primary_diagonal = []
secondary_diagonal = []
for row_col in range(len(matrix)):
    primary_diagonal.append(matrix[row_col][row_col])
    secondary_diagonal.append(matrix[row_col][-1 - row_col])
print(f"Primary diagonal: {', '.join([str(num) for num in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(num) for num in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")