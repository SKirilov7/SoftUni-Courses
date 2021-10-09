def get_magic_triangle(rows):
    matrix = [[1], [1, 1]]
    numbers_needed = 3

    for row in range(2, rows):
        current_matrix = []
        for col in range(numbers_needed):
            current_num = 0
            if is_valid_index(matrix, row-1, col):
                current_num += matrix[row-1][col]
            if is_valid_index(matrix, row-1, col-1):
                current_num += matrix[row-1][col-1]
            current_matrix.append(current_num)
        matrix.append(current_matrix)
        numbers_needed += 1
    return matrix


def is_valid_index(matr,r,c):
    return 0 <= r < len(matr) and 0 <= c < len(matr[r])


print(get_magic_triangle(5))