def print_row(num, current_row):
    whitespaces = num - current_row
    for w_space in range(whitespaces):
        print(' ', end='')
    for el in range(current_row):
        print('*', end=' ')
    print()


number = int(input())
for row in range(1, number):
    print_row(number, row)
for r in range(number, 0, -1):
    print_row(number, r)

