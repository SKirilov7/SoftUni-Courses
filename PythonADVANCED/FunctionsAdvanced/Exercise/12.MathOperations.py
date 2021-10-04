from collections import deque


def math_operations(*args,**kwargs):
    numbers = deque(args)
    while numbers:
        kwargs['a'] += numbers.popleft()
        if numbers:
            kwargs['s'] -= numbers.popleft()
        if numbers:
            current_num = numbers.popleft()
            if not current_num == 0:
                kwargs['d'] /= current_num
        if numbers:
            kwargs['m'] *= numbers.popleft()

    return kwargs



print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))