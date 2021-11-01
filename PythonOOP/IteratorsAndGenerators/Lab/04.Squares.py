def squares(n):
    current_num = 1
    while current_num <= n:
        yield current_num ** 2
        current_num += 1


print(list(squares(10)))
