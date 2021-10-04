rows,cols = [int(num) for num in input().split()]

matrix = [[0] * cols for row in range(rows)]


for row in range(rows):
    for col in range(cols):
        matrix[row][col] = f'{chr(97 + row)}{chr(97+col+row)}{chr(97+row)}'

for row in matrix:
    print(*row,sep = ' ')
