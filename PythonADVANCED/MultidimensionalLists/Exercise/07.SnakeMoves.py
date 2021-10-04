from collections import deque

rows,cols = [int(num) for num in input().split()]
matrix = [[0] * cols for row in range(rows)]
snake = deque(list(input()))

for row in range(rows):
    for col in range(cols):
        if not row % 2 == 0:
            ind = -1
            while 0 in matrix[row]:
                current_snake_element = snake.popleft()
                matrix[row][ind] = current_snake_element
                snake.append(current_snake_element)
                ind -= 1
        elif row % 2 == 0 or row == 0:
            current_snake_element = snake.popleft()
            matrix[row][col] = current_snake_element
            snake.append(current_snake_element)

for row in matrix:
    print(*row,sep='')