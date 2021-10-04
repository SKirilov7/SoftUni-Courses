def find_all_paths(matrix, directions='', row=0, col=0):
    if not is_valid_indexes(matrix, row, col) or matrix[row][col] == '*' or matrix[row][col] == 'V':
        return
    if matrix[row][col] == 'e':
        print(directions)
        return

    matrix[row][col] = 'V'

    find_all_paths(matrix, directions + 'U', row - 1, col)
    find_all_paths(matrix, directions + 'D', row+1, col)
    find_all_paths(matrix, directions + 'L', row, col-1)
    find_all_paths(matrix, directions + 'R', row, col+1)
    matrix[row][col] = '-'


def is_valid_indexes(matr,r,c):
    return 0 <= r < len(matr) and 0 <= c < len(matr[r])


rows = int(input())
cols = int(input())
field = [list(input()) for row in range(rows)]
find_all_paths(field)
